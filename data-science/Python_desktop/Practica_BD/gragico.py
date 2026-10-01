import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#---------------------------------------------#

surveys=pd.read_csv("surveys.csv")

 #.shape    =forma , filas y columnas del archivo

species_counts = surveys.groupby('species_id')['record_id'].count()

print(species_counts)

total_count = surveys.groupby('plot_id')['record_id'].nunique()

print(total_count)

plt.plot(species_counts)
#plt.show()


