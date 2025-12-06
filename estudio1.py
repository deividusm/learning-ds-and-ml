
""""
import pandas as pd

titulos = ["El Quijote","Cien años de soledad","La odisea"]
autores = ["Miguel de Cervantes","Gabriel Garcia Márquez", "Homero"]
años_de_publicacion = [1605,1967,-800]
libros_df = {"titulos": ["El Quijote","Cien años de soledad","La odisea"], 
             "autores": ["Miguel de Cervantes","Gabriel Garcia Márquez", "Homero"],
             "años_de_publicacion":[1605,1967,-800]}

df = pd.DataFrame(libros_df)
print(df)
"""
"""
import pandas as pd

# Datos proporcionados
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Sara'],
    'Edad': [25, 30, 22, 27],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Bilbao']
}

df = pd.DataFrame(data)
personas_sobre25 = df["Edad"] > 25
seleccion = df[personas_sobre25]
print(seleccion)
"""
"""
import pandas as pd
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Sara'],
    'Edad': [25, 30, 22, 27],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Bilbao']
}

df = pd.DataFrame(data)
#agregar columna "Profesión"
df["Profesión"] = ["Ingeniera", "Médico", "Estudiante", "Abogada"]
print(df)
"""

import pandas as pd
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Sara'],
    'Edad': [25, 30, 22, 27],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Bilbao']
}

df = pd.DataFrame(data)
#tomar serie de edades y pasar a lista
Tomar_edades = df["Edad"].tolist()
sumadas= []
for i in Tomar_edades:
    i += 10
    sumadas.append(i)
print(sumadas)
#añadir sumadas al dataframe
df["Edad_dentro_de_10_años"] = sumadas
print(df)

    

