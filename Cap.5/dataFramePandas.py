import pandas as pd
import numpy as np

np.random.seed(10)
#DATAFRAMES
#Array bidimensional (linhas e colunas)
#Cada coluna é umaa Series
#indexx representa as linhas
#columns representa as colunas

df = pd.DataFrame(
    index = ['A','B','C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data = np.random.randint(1, 50, size=(5,4))
    ) #5 linhas e 4 colunas com valores aleatórios entre 1 e 50

print(df)

# FAZENDO SLICING COM iloc (padrão numpy - indices numéricos)
print(df.iloc[0:2 ,:]) #Linhas 0 e 1, todas as colunas

#FAZENDO SLICING COM loc (padrão pandas - indices nomeados)
#Usa indices customizados
print(df.loc[['A','B'],['W','X','Y','Z']]) #Linhas A e B, todas as colunas

print(df.loc[['A','B'],['W','Y']])
