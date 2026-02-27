# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 23:24:25 2019

@author: Gorila
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos=pd.read_csv("C:/Programacion/python/Practica_BD/Bases de datos/Bretix/EU-referendum-result-data.csv")

muestra=datos.iloc[0:10,[4,5]]
#print(muestra)

colors  = ("dodgerblue","salmon", "palevioletred", 
           "steelblue", "seagreen", "plum", 
           "blue", "indigo", "beige", "yellow")

i=0

for col in muestra:
    
    sizes=muestra[col].value_counts()
    
    grafico=muestra[col].value_counts().plot(kind="pie",
                   colors=colors,autopct="%1.1f%%",
                   startangle=30,radius=1.5,center=(0.5,0.5),
                   textprops={"fontsize":12},frame=False,
                   pctdistance=.65)
    
    labels=sizes.index.unique()
    
    plt.gca().axis("equal")
    plt.title(muestra.columns[i],weight="bold",size=14)
    
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.85)
    
    i=i+1
    
    plt.show()