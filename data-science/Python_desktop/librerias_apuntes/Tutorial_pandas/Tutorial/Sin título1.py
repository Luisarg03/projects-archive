import matplotlib.pyplot as plt
import pandas as pd


datos=pd.read_csv("C:/Programacion/python/Practica_BD/Bases de datos/Bretix/EU-referendum-result-data.csv")

muestra=datos.iloc[0:10,[4,5]]


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = datos.iloc[0:10,4]
print(labels)


explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(muestra, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()