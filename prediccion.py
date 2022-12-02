import pandas as pd

def main():
    semanas = pd.read_csv('./data/semanas.csv', sep=';', encoding='latin-1')

    ingredientes = [column for column in semanas.columns]

    media = {}
    for ingrediente in ingredientes:
        suma = semanas[ingrediente].sum()
        media[ingrediente] = suma/53

    valido = False
    while not valido:
        predicciones = {}
        n = input('Semana (0-52): ')
        try:
            n = int(n)
            row = semanas.iloc[n]
            for ingrediente in ingredientes:
                predicciones[ingrediente] = ((row[ingrediente]+media[ingrediente])/2).round(2)
            valido = True
        except:
            print('Ingrese un número válido')
            valido = False
    print(predicciones)

if __name__ == '__main__':
    main()
    