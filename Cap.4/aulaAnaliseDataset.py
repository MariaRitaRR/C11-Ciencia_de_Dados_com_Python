import numpy as np

#CARREGANDO DATASETS COM NUMPY
ds = np.loadtxt('space.csv',
                delimiter=';',
                dtype=str,
                encoding='utf-8') 
# Carrega o dataset space.csv em um array numpy
# O parâmetro delimiter define o separador de colunas, dtype define o tipo de dados e encoding define a codificação do arquivo

print(ds)  # Exibe o conteúdo do dataset carregado
print(ds[0,:]) # Exibe a primeira linha do dataset

#Calculando a média de uma missão espacial
#Slicing para extrair a coluna de custo (Cost)
ds_cost = ds[1:,6] # Exclui o cabeçalho e extrai a coluna de custo
# Converte os valores de custo para float
ds_cost = ds_cost.astype(float)
# Calcula a média do cuusto de missão espacial
media_cost = np.mean(ds_cost[ds_cost > 0])  # Exclui valores negativos ou zero antes de calcular a média

print(f'Média de custo das missões espaciais: {media_cost:.2f} milhões de dólares')  # Exibe a média de custo formatada

