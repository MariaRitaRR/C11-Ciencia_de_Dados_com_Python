import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('space.csv', delimiter=';')

df_roscosmos = df[df['Company Name'].str.strip() == 'Roscosmos']

sucessos = df_roscosmos[df_roscosmos['Status Mission'].str.strip() == 'Success'].shape[0]
falhas = df_roscosmos[df_roscosmos['Status Mission'].str.strip() != 'Success'].shape[0]

valores = [sucessos, falhas]
labels = ['Sucesso', 'Falha']
cores = ['green', 'red']

plt.figure(figsize=(6,6))
plt.pie(valores, labels=labels, autopct='%1.1f%%', colors=cores, startangle=90)
plt.title('Missões da Roscosmos: Sucesso vs Falha')
plt.axis('equal')
plt.show()