import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

surveys_df=pd.read_csv("C:/Programacion/python/Practica_BD/Bases de datos/Nueva carpeta/surveys.csv");


species_counts = surveys_df.groupby('species_id')['record_id'].count()
print(species_counts)
print()
#grafica de estadisticas

#species_counts.plot(kind="bar");

total_count = surveys_df.groupby('plot_id')['record_id'].nunique()
# También grafiquemos eso
total_count.plot(kind='bar');








plot.show()