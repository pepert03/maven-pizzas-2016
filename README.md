Predicción Maven Pizzas 2016
=================

## Introducción
Instalar librerías de Python para el análisis de datos:
```
pip install -r requirements.txt
```
Todos los archivos necesarios se encuentran en la carpeta `data`, los nuevos son:
* `orders.csv`: Archivo con los pedidos
* `order_details.csv`: Archivo con los detalles de los pedidos

## Ejecución
**Nota**: El tiempo de ejecución de `etl.py` es de 3 minutos aprox., los datasets obtenidos ya están guardados en la carpeta `data`, no hace falta ejecutar `etl.py`para hacer la predicción.

Para analizar los datos, se puede ejecutar el script `etl.py`, generando los archivos:
* `orders_n.csv`: Archivo limpio de pedidos
* `order_details_n.csv`: Archivo limpio de detalles de pedidos
* `data/dias.csv`: Contiene la cantidad ingredientes vendidos por día.
* `data/semana.csv`: Contiene la cantidad de ingredientes vendidos por semana.

El archivo `informe.py` muestra por pantalla un informe de calidad de los datos, mostrando el tipo de dato y  la cantidad de Null por columna.

## Predicción
Para predecir los ingredientes necesarios para una semana, se puede ejecutar el script `predict.py`, e introducir la semana a predecir. Ejemplo:
```
Semana (0-52): 1
```
Generando un diccionario con los ingredientes necesarios para la semana.
