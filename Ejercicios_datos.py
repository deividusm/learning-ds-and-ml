import pandas as pd

df = pd.read_csv("medallas.csv")

tamaño = df.shape
print(f"Posee {tamaño[0]} filas y {tamaño[1]} columnas")
info  = df.info()
print(info)
rellenar = df.fillna(0)
print(rellenar)

top3 = df.sort_values("Total", ascending= False).head(3)
print(top3)



"""
print(df.isnull().sum()) #Con esto puedo saber que puedo rellenar completamente toda las filas que son nulas pues donde unicamente faltan son en las medallas rellenamos con 0

rellenar_valores = {"Gold": 0, "Silver": 0, "Bronze": 0}
df_rellenado = df.fillna(rellenar_valores)


#tomemos la columna total para lograr conocer los paises con mayor numero de medallas (los 3)

medallas_total = df["Total"]

print(medallas_total)

agarrar_los_3_mejores = medallas_total.nlargest(3).index
print(agarrar_los_3_mejores)

paises = df["Pais"]
print(f"El primer lugar es para {paises[25]}\nEL segundo lugar es para {paises[72]}\nEl tercer lugar es para {paises[73]}")
print(df_rellenado.isnull().sum()) #ya no quedan filas nulas todas estan completas
print(df_rellenado)
"""