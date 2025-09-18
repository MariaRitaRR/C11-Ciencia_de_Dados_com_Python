#PLOTS COM MATPLOTLIB
#grafico de linha
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#craiando dos valores de x e y
x = np.array([1, 2, 3, 4, 5])
y = x*2
y2 = x*x
#explicando dos exios x e y
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

plt.subplot(1,2,1)
plt.plot(x, y, '*:r',linewidth=3, markersize=10)

plt.subplot(1,2,2)
plt.plot(x, y2, 's--g',linewidth=3, markersize=10)

#plotando o grafico
#plt.plot(x, y, '*:r',x, y2, 's--gn',linewidth=3, markersize=10)
plt.show()

