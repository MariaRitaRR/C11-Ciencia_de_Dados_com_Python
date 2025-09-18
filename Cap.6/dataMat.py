import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Scatter (dispersão)
dfPaises = pd.read_csv('paises.csv', delimiter=';')
print(dfPaises.columns)

# Extraindo os 6 maiores países em área do mundo
dfMaioresPaiese = dfPaises.nlargest(6, 'Area (sq. mi.)')
print(dfMaioresPaiese['Country'])

# Traçar um Scatter Plot que ilustre o GPD desses países[
plt.scatter(dfMaioresPaiese['Country'],dfMaioresPaiese['GDP ($ per capita)'],s=500)
plt.show()


#BAR PLOT
# Extraindo os 5 páises com maoir renda per capita
dfRenda = dfPaises.nlargest(5, 'GDP ($ per capita)')
print(dfRenda['Country'])
plt.bar(dfRenda['Country'],dfRenda['GDP ($ per capita)'], color='orange')
plt.show()



#GRAFICO EM PIZZA
dfNCost = dfPaises[dfPaises['Coastline (coast/area ratio)']==0]
print(dfNCost['Country'])
qntNCoast = len(dfNCost)
qntCoast = len(dfPaises) - qntNCoast
plt.pie([qntNCoast,qntCoast],labels=['Paises sem costa', 'Paises com costa',],autopct='%1.1f%%')
plt.show()

