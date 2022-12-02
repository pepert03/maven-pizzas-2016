import pandas as pd

# order_id,date,time
orders = pd.read_csv('./data/orders.csv', sep=';', encoding='latin-1')

# order_details_id,order_id,pizza_id,quantity
order_details = pd.read_csv('./data/order_details.csv', sep=';', encoding='latin-1')


print('INFORME DE TOPOLOGÍA DE DATOS')
# tipo de dato de cada columna
print('orders')
for columna in orders.columns:
    print(columna, orders[columna].dtype)
print('order_details')
for columna in order_details.columns:
    print(columna, order_details[columna].dtype)

# cantidad de nulls y nan
print('Numero de nulls en orders: ')
print(orders.isna().sum())
print('Numero de nulls en order_details: ')
print(order_details.isna().sum())