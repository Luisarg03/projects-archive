import pandas as pd
import numpy as np

datos=pd.read_csv("C:/Programacion/python/Practica_BD/Bases de datos/Bretix/EU-referendum-result-data.csv")

#print(datos.info())

# .iloc[row]
#print(datos.iloc[0:5]) 


#rangos       filas y columnas
#print(datos.iloc[0:5,5:8])

#elijiendo filas
#print(datos.iloc[[0,3,6],])

#elijiendo columnas
#print(datos.iloc[:,0:5])


#print(datos.info())

#elijo rango de filas y columnas especificas
muestra=datos.iloc[0:10,[4,5]]

print(muestra)