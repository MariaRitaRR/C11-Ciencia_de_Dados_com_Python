#  5. Crie uma matriz de tamanho 4x4 formada por números aleatórios inteiros 
# entre 1 e 50 (use seed = 10 antes)
#  Mostre o resultado da média de cada linha e cada coluna da matriz 
# gerada 
# Apresente o maior valor das médias das linhas e também das colunas
#  Mostre a quantidade de aparições de cada um dos números gerados na 
# matriz. Em seguida, mostre apenas os números que aparecem 2 vezes

import numpy as np
np.random.seed(10)
mtz = np.random.randint(1,51,(4,4))
print(f"Media das linhas :{mtz.mean(axis=1)}")
print(f"Media das colunas :{mtz.mean(axis=0)}") 
print(f"Maior valor das médias das linhas :{mtz.mean(axis=1).max()}")
print(f"Maior valor das médias das colunas :{mtz.mean(axis=0).max()}")

valores, contagens = np.unique(mtz, return_counts=True) 
aparicoes_2_vezes = valores[contagens == 2]
print(f"Números que aparecem 2 vezes: {aparicoes_2_vezes}")