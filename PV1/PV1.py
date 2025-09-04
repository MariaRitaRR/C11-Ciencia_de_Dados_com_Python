import numpy as np

ds = np.loadtxt('shopping_trends.csv', delimiter=',',
                dtype=str, encoding='utf-8')

#Questão 1: Mostre qual a média de idade dos homens
homens_mask = ds[1:,2] == 'Male'
homens_data = ds[1:][homens_mask]
idade_homens =ds[1:,1].astype(float)
media_idade_homens = np.mean(idade_homens)
print(f'Media de idade dos homens: { media_idade_homens:.2f} anos')

#Questão 2: Mostre quanto cliente gastaram mais que a media de compras
gastos = ds[1:,5].astype(float)
media_gastos = np.mean(gastos)
clientes_acima_media = gastos>media_gastos
print(len(f'Clientes que gastaram mais que a media de compras : {clientes_acima_media}'))

#Questão 3:Mostre qual a porcentagem de vendas do item menos vendido da loja
itens = ds[1:,4]
itens_unicos, cont_itens= np.unique(itens, return_counts=True)
cont_item_menos_comprado = np.min(cont_itens)
percentual_item = cont_item_menos_comprado / len(itens)*100
print(f'Percentual do item menos comprado: {percentual_item:.2f}%')

#Questão 4:Mostre qual a porcentagem de vendas que tiveram algum tipo de desconto
desconto = ds[1:,13]
desconto_sim = desconto[desconto == 'Yes']
porcentagem_desconto = len(desconto_sim)/(len(desconto))*100
print(f'Percentual doe vendas que tiveram desconto: {porcentagem_desconto:.2f}%')

#Questão5: Mostre qual a cor de roupa mais popular vo verão
verao_mask = ds[1:,9] =='Summer'
verao_data = ds[1:][verao_mask]
cores_verao = verao_data[:,8]
cores_unicas, cont_cores = np.unique(cores_verao, return_counts=True)
cor_mais_popular = cores_unicas[np.argmax(cont_cores)]
print(f'A cor mais popular é: {cor_mais_popular}')


