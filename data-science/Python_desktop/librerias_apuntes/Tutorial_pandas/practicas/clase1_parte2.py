import pandas as pd

surveys_df=pd.read_csv("C:/Programacion/python/Practica_BD/Bases de datos/Nueva carpeta/surveys.csv");

print("nombre de las columnas")
print(surveys_df.columns)
print()

print("valores existentes en la columna species_id")
print(pd.unique(surveys_df["species_id"]))

#indica los distintos valores que aparecen en la columna especificada
#no salen todos los valores, solo las variantes



##creo una lista con los tipos de variables que aparecen en la columna plot_id
print()
print("valores existentes en la columna plot_id")

site_names=pd.unique(surveys_df["plot_id"]);

print(site_names)
print()

#??cual es la diferencia? :S (cuento la cantidad de tipos de variables que salen,especies en este caso)
#
print(len(site_names))
print("Numero de especies registradas")
print(surveys_df["plot_id"].nunique()) 
print()
print()
print("Primeras estadisticas")
print("calcular algunas estadísticas básica de todos los datos en una columna")
print()
print(round(surveys_df["weight"].describe(),2))
#mean=media    std=desviacion estandar
print("podemos calcular una metrica particular especificandola")
print("max")
print(surveys_df["weight"].max())
print("min")
print(surveys_df["weight"].min())

#.groupdby()  =  agrupar datos por x caracteristica, la que especifiquemos
#
dato_agrupado=surveys_df.groupby("sex")

print(round(dato_agrupado.count()))
print()
#agrupamos por dos caracteristicas, haciendo dos columnas

#group_data2=surveys_df.groupby(["sex","plot_id"])

#print(round(group_data2.mean()))


group_specie=surveys_df.groupby("species_id")

print(round(group_specie["weight"].describe()))

print()

#Conteo de muestras por cada especies, combinando el metodo groupby+count.
#hay varias maneras de hacerlo

specie_count=surveys_df.groupby("species_id")["record_id"].count()
print(specie_count)

print()
#podemos contar en cuantas lineas sale x ...
print("Conteo de lineas ocupadas por la especie DO en el data frame")
print(surveys_df.groupby('species_id')['record_id'].count()['DO'])