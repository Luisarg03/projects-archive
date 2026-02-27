import pandas as pd

#llamar a una funcion dentro de la biblioteca
#nombrebiblioteca.funcion
#alias.funcion

#.CSV (comma-separated-Values), valores separados por comas.
#
#Que es un dataframe?
#analogo a la hoja de calculo del excel, es una estructura de datos almacenados en columnas
#
#leer el dataframe

surveys_df=pd.read_csv("C:/Programacion/python/Practica_BD/Bases de datos/Nueva carpeta/surveys.csv")

#print(surveys_df);

#la primera columna del dataframe lleva los indices de los datos, inidca la posicion de los datos en el D.Frame.

print(type(surveys_df)) #funcion type, indica el tipo de variable/archivos que es

print(surveys_df.dtypes) #dtypes. indica el tipo de valores que contiene el dataframe

print()

print(surveys_df.columns) #nombres de todas las columnas del dataframe

print()

print(surveys_df.head(21)) #accedo a las primeras filas del dataframe, puedo asignar 								cantidad de filas que quiero ver, recorda que el frame se 								guia por indices y empieza desde 0.

print(str(surveys_df.shape)+"forma del dataframe")
 #indica cantidad de filas y columnas del frame
print()
print(surveys_df.tail()) #muestra las ultimas 5 filas del data frame

print("ahora con valor 10")

print(surveys_df.tail(10)) #le digo qu equiero ver las ultimas 10 filas del data frame

