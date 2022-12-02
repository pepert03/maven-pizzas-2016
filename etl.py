import pandas as pd


# order_id,date,time
orders = pd.read_csv('./data/orders_n.csv', sep=',', encoding='latin-1')

# order_details_id,order_id,pizza_id,quantity
order_details = pd.read_csv('./data/order_details_n.csv', sep=',', encoding='latin-1')

# pizza_type_id,name,category,ingredients
pizza_types = pd.read_csv('./data/pizza_types.csv', sep=',', encoding='latin-1')

# pizza_id,pizza_type_id,size,price
pizza_price = pd.read_csv('./data/pizzas.csv', sep=',', encoding='latin-1')

def limpiar_datos():
    # order_id,date,time
    orders = pd.read_csv('./data/orders.csv', sep=';', encoding='latin-1')

    # order_details_id,order_id,pizza_id,quantity
    order_details = pd.read_csv('./data/order_details.csv', sep=';', encoding='latin-1')

    # pizza_type_id,name,category,ingredients
    pizza_types = pd.read_csv('./data/pizza_types.csv', sep=',', encoding='latin-1')

    # pizza_id,pizza_type_id,size,price
    pizza_price = pd.read_csv('./data/pizzas.csv', sep=',', encoding='latin-1')

    
    for i in range(len(orders)):
        x = orders['date'][i]
        if not pd.isna(x):
            try: 
                a = pd.to_datetime(float(x)+3600, unit='s')
            except:
                a = pd.to_datetime(x)
        orders['date'][i] = str(a).split(' ')[0]
    orders.sort_values(by=['order_id'], inplace=True)

    for i in range(len(order_details)):
        quantities = [[1,'One','one',-1,'1','-1',],[2,'Two','two',-2,'2','-2']]
        try:
            n = int(order_details['quantity'][i])
        except:
            for q in quantities:
                if order_details['quantity'][i] in q:
                    n = q[0]
        if pd.isna(order_details['quantity'][i]):
            n = 1
        order_details['quantity'][i] = n

        if not pd.isna(order_details['pizza_id'][i]):
            pizza_t = order_details['pizza_id'][i]
            pizza_t = pizza_t.replace('@','a')
            pizza_t = pizza_t.replace('0','o')
            pizza_t = pizza_t.replace('3','e')
            pizza_t = pizza_t.replace('-','_')
            pizza_t = pizza_t.replace(' ','_')
        order_details['pizza_id'][i] = pizza_t
       
    order_details.sort_values(by=['order_details_id'], inplace=True)

    order_details.dropna(inplace=True)
    orders.dropna(inplace=True)
    order_details.to_csv('./data/order_details_n.csv', sep=',', encoding='latin-1', index=False)
    orders.to_csv('./data/orders_n.csv', sep=',', encoding='latin-1', index=False)



def pizzas_por_dia(ingredientes, pizza_info):
    dias = pd.DataFrame(columns=[])
    for ingredient in ingredientes:
        dias[ingredient] = 0.0
    for i in range(367):
        dias.loc[i] = 0.0
    for i in range(len(orders)):
        x = orders['date'][i]
        a = pd.to_datetime(x, format='%Y-%m-%d')
        dia = a.dayofyear
        for _,row in order_details[order_details['order_id'] == orders['order_id'][i]].iterrows():
            quantities = [[1,'One','one',-1,'1','-1',],[2,'Two','two',-2,'2','-2']]
            try:
                n = int(row['quantity'])
            except:
                for q in quantities:
                    if row['quantity'] in q:
                        n = q[0]
            for _ in range(n):
                pizza_t = row['pizza_id']
                for _,row in pizza_price.iterrows():
                    if pizza_t == row['pizza_id']:
                        pizza_t = row['pizza_type_id']
                        size = row['size']
                        if size == 'S':
                            size = 0.75
                        elif size == 'M':
                            size = 1
                        elif size == 'L':
                            size = 1.25
                        elif size == 'XL':
                            size = 1.5
                        elif size == 'XXL':
                            size = 2
                        break
                ingredientes_p = pizza_info[pizza_t].split(',')
                for ingrediente in ingredientes_p:
                    dias.iloc[dia][ingrediente] += size
    return dias

def pizzas_por_semana(dias,ingredientes):
    semanas = pd.DataFrame(columns=[])
    for ingredient in ingredientes:
        semanas[ingredient] = 0.0
    for i in range(53):
        semanas.loc[i] = 0.0
    for i in range(len(dias)):
        n = i//7
        semanas.iloc[n] += dias.iloc[i]
    return semanas

def main():

    print(orders.isna().sum())
    print(order_details.isna().sum())

    pizza_info = {}
    for i in range(len(pizza_types)):
        pizza_info[pizza_types['pizza_type_id'][i]] = pizza_types['ingredients'][i]
    
    ingredientes = []
    for i in pizza_types['ingredients']:
        ingred = i.split(',')
        for j in ingred:
            if j not in ingredientes:
                ingredientes.append(j)

    dias = pizzas_por_dia(ingredientes, pizza_info)
    dias.to_csv('./data/dias.csv', sep=';', encoding='latin-1', index=False)
    print(dias)
    semanas = pizzas_por_semana(dias,ingredientes)
    semanas.to_csv('./data/semanas.csv', sep=';', encoding='latin-1', index=False)
    print(semanas)


if __name__ == '__main__':
    main()
    # semanas = pd.read_csv('./data/semanas.csv', sep=';', encoding='latin-1')
    # dias = pd.read_csv('./data/dias.csv', sep=';', encoding='latin-1')