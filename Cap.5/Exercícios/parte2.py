import pandas as pd
import numpy as np

# 6 calcule a média dos elementos da coluna X que são menores que 30

np.random.seed(10)

df = pd.DataFrame(
    index = ['A','B','C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data = np.random.randint(1, 50, size=[5,4])
    )
media_x = df['X'][df['X']<30].mean()
print(f"Media da coluna X : {media_x:.2f}")


# 7 Utilizando do mesmo DataFrame apresente a média dos elementos da
# linha D usando a função loc como base e a soma dos elementos da linha E
# usando a função iloc como base

media_d = df.loc['D'].mean()
soma_e = df.iloc[4].sum()
print(f"Média da linha D: {media_d:.2f}")
print(f"Soma da linha E: {soma_e}")

#8 Faça um Slicing na matriz mostrando apenas as linhas A, C e E
# juntamente com as colunas X e Y Em seguida, mostre qual seria a soma dos
# elementos de cada uma destas linhas e cada uma destas colunas

slicing = df.loc[['A','C','E'],['X','Y']]
print(slicing)
print(f"Soma das linhas:\n{slicing.sum(axis=1)}")
print(f"Soma das colunas:\n{slicing.sum(axis=0)}")