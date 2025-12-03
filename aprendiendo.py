import pandas as pd
#ller un acrhivo CSV en un DataFrame de pandas que tengo en vs que se llama Precipitaciones.csv
df = pd.read_csv('Precipitaciones.csv')
print(df.tail())

shape = df.shape
print(f'El DataFrame tiene {shape[0]} filas y {shape[1]} columnas.')