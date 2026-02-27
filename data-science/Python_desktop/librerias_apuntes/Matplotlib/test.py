import matplotlib.pyplot as plt
import numpy as np

#figure = ventana / axes=grafico

#Creamos dos ventanas y nombres
plt.figure('ventana1') 
plt.figure('ventana2') 

#valroes aleatorios
a = np.random.rand(100)
b = np.random.rand(100)

#llamo a la ventana
plt.figure('ventana1')

#asigno el tipo de grafico que voy a usar
plt.scatter(a,b) #grafico puntos xD

#segunda ventana
plt.figure('ventana2') 
plt.plot(a,b) #grafico lineas

plt.show()