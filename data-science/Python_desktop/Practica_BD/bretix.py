import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importamos la base de datos

bd=pd.read_csv("EU-referendum-result-data.csv")

#print(bd);

#toda la base de datos esta en esta variable / array

#suma de quien esta a favor de permanecer en la UE y quien no

# vamos a sumar quien esta a favor de la UE y quien no
noUE = bd["Leave"].sum();
siUE = bd["Remain"].sum();

print("no UE:"+str(noUE)+" votantes | si UE "+str(siUE)+" votantes")
print()
#print("no UE: {} votantes | si UE {} votantes".format(noUE, siUE))#
#
#.format da el formato especifico

#Calculo de porcentaje de SI y NO

porcensiUE=siUE/(siUE+noUE)*100;
porcennoUE=noUE/(siUE+noUE)*100;

print("Porcentaje de votos en contra de permanecer en la UE: "+str(round(porcennoUE,2))+"%");
print()
print("Porcentaje de votos a favor de permanecer en la UE: "+str(round(porcensiUE,2))+"%");

#grafica de la base de datos