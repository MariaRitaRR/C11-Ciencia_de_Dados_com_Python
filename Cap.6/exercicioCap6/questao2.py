import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('space.csv', delimiter=';')

df_usa = df[df['Location'].str.contains('USA', case=False, na=False)]
df_china = df[df['Location'].str.contains('China', case=False, na=False)]

empresas_usa = df_usa['Company Name'].unique()
empresas_china = df_china['Company Name'].unique()

num_empresas_usa = len(empresas_usa)
num_empresas_china = len(empresas_china)

paises = ['USA', 'China']
valores = [num_empresas_usa, num_empresas_china]

plt.figure(figsize=(8,6))
plt.bar(paises, valores, color=['blue', 'red'])
plt.title('Número de Empresas de Lançamento de Foguetes por País')
plt.ylabel('Número de Empresas')
plt.show()