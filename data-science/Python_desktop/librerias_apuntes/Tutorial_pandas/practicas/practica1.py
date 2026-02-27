import pandas as pd

surveys_df=pd.read_csv("C:/Programacion/python/Practica_BD/Bases de datos/Nueva carpeta/surveys.csv");

#print(grouped_data_peso['weight'].describe())
print(surveys_df.head(10))
#ordena por especie, y cuenta los record_id de cada especie.
species_counts = surveys_df.groupby('species_id')['record_id'].count()
print(species_counts)


#lo mismo, pero especifico que quiero saber cantidad de record_id de la especie DO
print("Cuento especie DO")
conteo_do=surveys_df.groupby('species_id')['record_id'].count()['DO']
print(conteo_do)