import pandas as pd

data = {
    "Id_producto": [1001, 1002, 1003, 1003],
    "Cantidad_vendida": [30, None, 25, 25],
    "Precio": [20.5, 15.0, None, 22.5]
}

df = pd.DataFrame(data)

#valores_nulos = df.isnull()
#print(valores_nulos)

#cantidad_de_valores_nulos = df.isnull().sum()
#print(cantidad_de_valores_nulos)

#df_eliminados = df.dropna()
#print(df_eliminados)
#elimina las filas donde hay valores nulos


#remplazar los valores nulos por 0
#valores_nuevos = {"Cantidad_vendida": 0}
#df_rellenados = df.fillna(valores_nuevos)

#remplazar los valores por el promedio
valores_nuevos = {"Cantidad_vendida": 0, "Precio": df["Precio"].mean()}
df_rellenados = df.fillna(valores_nuevos) #rellenar con algun diccionario

#como modificar el tipo de dato de alguna serie de mi dataframe

df_rellenados["Cantidad_vendida"] = df_rellenados["Cantidad_vendida"].astype(int)
#astype sirve para cambiar el tipo de dato
print(df_rellenados)


df_unicos = df_rellenados.drop_duplicates(subset="Id_producto")
print(df_unicos)


# ejemplo de ejercicio
import pandas as pd

data = {
    'ID': [1, 2, 3, 4],
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D'],
    'Cantidad': [10, 20, 30, 40],
    'Precio': [100, None, 300, None]
}

df = pd.DataFrame(data)

precio= {"Precio": df["Precio"].mean()}

rellenar_fila_precio = df.fillna(precio)


#filtrar datos

serie = pd.Series([5,10,15,20,25])
print(serie)

filtro = serie > 15 # bool

serie_filtrada = serie[filtro] #ingresamos el booleano y nos devolveria los datos similar a indexar
print(serie_filtrada)

serie2 = pd.Series (["banana", "pera","melon","manzana"])
que_es = type(serie2)
que_es_dentro = type(serie2[0])

letra_m = serie2.str.contains("m")
print(serie2[letra_m])