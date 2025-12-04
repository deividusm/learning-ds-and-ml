import pandas as pd

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

serie = pd.Series(lista)

filtro = serie > 10
serie_filtrada = serie[filtro]
print(serie_filtrada)


frutas = pd.Series(["manzana", "banana", "cereza", "durazno", "frambuesa"])

frutas_con_e = frutas.str.contains("e")
print(frutas[frutas_con_e])