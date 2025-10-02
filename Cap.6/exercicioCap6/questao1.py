import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('paises.csv', delimiter=';')

df['Region'] = df['Region'].str.strip()
df_norte = df[df['Region']== 'NORTHERN AMERICA']

paises = df_norte['Country']
natalidade = df_norte['Birthrate']
mortalidade = df_norte['Deathrate']


plt.figure(figsize=(12,6))
plt.plot(paises, natalidade, 'g-o', label = 'Natalidade')
plt.plot(paises, mortalidade, 'r-s', label = 'Mortalidade')
plt.title('Taxa de Natalidade e Mortalidade - América do Norte')
plt.xlabel('Países')
plt.ylabel('Taxa (por mil habitantes)')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()

plt.show()