import pandas as pd
ventas = [120, 150, 90, 200, 210, 130, 160]
indices_dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

serie_numeros = pd.Series(ventas, indices_dias)

suma_total_ventas = serie_numeros.sum()
print(suma_total_ventas)
dia_de_mayor_venta = serie_numeros.max()
print(dia_de_mayor_venta)
promedio_ventas_en_la_semana = serie_numeros.mean()
print(promedio_ventas_en_la_semana)