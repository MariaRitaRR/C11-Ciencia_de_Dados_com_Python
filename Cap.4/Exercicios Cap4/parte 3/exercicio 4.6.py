# Baseado nos commandos que vimos até o momento e no Dataset
#  fornecido, crie scripts em Python que respondam às seguintes
#  perguntas:





import numpy as np

ds = np.loadtxt('space.csv',
                delimiter=';',
                dtype=str,
                encoding = 'utf-8')
header = ds[0]
data = ds[1:]

#  Apresente a porcentagem de missões que deram certo
missoes_sucesso = data[:,7] == 'Success'
total_missoes = np.size(data,0)

porcentagem_sucesso = (np.sum(missoes_sucesso) / total_missoes) * 100
print(f'Porcentagem de missões que deram certo: {porcentagem_sucesso:.2f}%')

#  Qual a media de gastos de uma missão especial se baseando em missões que possuam valores disponíveis (> 0)?
ds_cost = data[:,6].astype(float)
media_cost = np.mean(ds_cost[ds_cost >0])
print(f'Média de custo das missões espaciais: {media_cost:.2f} milhões de dólares')

#  Encontre quantas missões espaciais neste Dataset foram realizadas pelos Estados Unidos (EUA)
missoes = data[2]
missoes_EUA = np.char.find(missoes, 'USA')
total_missoes_EUA = np.sum(missoes_EUA)
print(f'Total de missões realizadas pelos EUA: {total_missoes_EUA}')

#  Encontre qual foi a missão mais cara realizada pela empresas “SpaceX”
spaceX_missoes = data[np.char.find(data[:,1], 'SpaceX')]
custo_spaceX = spaceX_missoes[:,6].astype(float)
arg_missao_mais_cara = np.argmax(custo_spaceX)
missao_mais_cara = spaceX_missoes[arg_missao_mais_cara]

print(f'Missão mais cara realizada pela SpaceX: Localização: {missao_mais_cara[2]}, Data: {missao_mais_cara[3]} Detalhes: {missao_mais_cara[4]} Status Rocket: {missao_mais_cara[5]} Custo: {missao_mais_cara[6]} milhões de dólares Status Missão: {missao_mais_cara[7]}')

#  Mostre o nome das empresas que já realizaram missões espaciais, juntamente com suas respectivas quantidades de missões (use o for no final para mostrar as informações
empresas, contagem = np.unique(data[:,1], return_counts=True)
print('Empresas que realizaram missões espaciais e suas respectivas quantidades de missões:')
for empresa, qtd in zip(empresas, contagem):
    print(f'Empresa: {empresa}, Quantidade de missões: {qtd}')