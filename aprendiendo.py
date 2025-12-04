import pandas as pd

data = {
    'ID': [1, 2, 3, 4, 5],
    'Producto': ['Producto A', 'Producto B', None, 'Producto D', 'Producto E'],
    'Cantidad': [10, 20, 30, None, 50],
    'Precio': [100, 200, 300, 400, None]
}
df = pd.Dataframe(data)
contar_valores_nulos = df.isnull().sum()
print(contar_valores_nulos)