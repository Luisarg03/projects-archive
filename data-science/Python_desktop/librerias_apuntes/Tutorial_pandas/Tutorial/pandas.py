
import pandas as pd
import sys
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#series: podemos almacenar arrays o vectores con etiquetas o indices. (si no asiganmos indices o etiquetas pandas las asigan internamente )

# s = Series(data, index=index)
# 
# creando una serie y pandas asigna automaticamente indices
# 

#serie = pd.Series(np.random.randn(10))
#print(type(serie))
 

# creando una serie con indices asignados por nosotros
#serie = pd.Series(np.random.randn(4), index = ['itzi','kikolas','dieguete','nicolasete'])
#print(u'Serie con índices definidos \n{} \n'.format(serie))
#print(type(serie))


# creando una serie usando indices que sos fechas
#serie = pd.Series(np.random.randn(31), index = pd.date_range('2013/01/01', periods = 31))
#print(u'Serie temporal con índices de fechas \n{} \n'.format(serie))
#print(type(serie))

