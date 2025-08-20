#  4. Crie uma matriz de tamanho qualquer. Extraia seu número de linhas e 
# colunas, multiplique-os, e diga se esta matriz poderia se tornar um vetor 
# unidimensional com número par ou ímpar de elementos

import numpy as np

mtz = np.array([[1, 2, 3], [4, 5, 6]])
linhas, colunas = mtz.shape
produto = linhas * colunas
if produto % 2 == 0:
    print(f"A matriz tem {linhas} linhas e {colunas} colunas, totalizando {produto} elementos, que é um número par.")
else:
    print(f"A matriz tem {linhas} linhas e {colunas} colunas, totalizando {produto} elementos, que é um número ímpar.")