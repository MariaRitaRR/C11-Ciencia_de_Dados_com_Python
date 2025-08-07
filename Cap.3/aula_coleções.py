#EXEMPLOS DE TUPLAS ()
tupla = ('Goku', 'Vegeta', 'Trunks', 'Gohan')

#MOSTRANDO ELEMENTOS DA TUPLA
print(tupla) #forma mais simples e objetiva de printar uma tupla

#ALTERAR ELEMENTOS DA TUPLA

# tupla[0] = 'Bulma' #isso não funciona, pois tuplas são imutáveis    

#QUAL A VANTAGEM DE USAR TUPLAS?
#Tuplas são imutáveis, o que significa que uma vez criadas, não podem ser alteradas. 
#Isso as torna mais seguras para armazenar dados que não devem ser modificados. 
#Além disso, elas podem ser usadas como chaves em dicionários,
#o que não é possível com listas, já que listas são mutáveis.

#SLICING DE ELEMENTOS (FATIAR ELEMENTOS)
print(tupla[1:3]) #Vegeta e Trunks
print(tupla[2:]) #TrUnks e Gohan (A partir do índice 2 tudo para frente)
print(tupla[-2]) #Trunks (Contando de trás para frente, -1 é o último elemento, -2 é o penúltimo)
print(tupla[:2]) #Goku e Vegeta (Do início até o índice 2, não incluindo o índice 2)


#FUNÇÕES PRE-PRONTAS
print (len(tupla)) #4 (Mostra o tamanho da tupla)
print (max(tupla)) #Vegeta (Mostra o maior elemento da tupla, baseado na ordem alfabética)
print (min(tupla)) #Gohan (Mostra o menor elemento da tupla, baseado na ordem alfabética)
print(sorted(tupla)) #['Gohan', 'Goku', 'Trunks', 'Vegeta'] (Mostra a tupla ordenada em ordem alfabética porém como uma lista)

#Exemplos com Listas []
lista = ['Goku', 'Vegeta', 'Trunks', 'Gohan']

#MOSTRANDO ELEMENTOS DA LISTA
#listas são mutáveis, ou seja, podem ser alteradas

print(lista) #forma mais simples e objetiva de printar uma lista

#INSERIR ELEMENTOS NA LISTA
lista.append('Bulma') #Adiciona 'Bulma' no final da lista (apendar)
lista.insert(1, 'Kuririn') #Adiciona 'Kuririn' no início da lista (inserir na posição 1)  
print(lista) #['Kuririn', 'Goku', 'Vegeta', 'Trunks', 'Gohan', 'Bulma']

#ALTERAR ELEMENTOS DA LISTA
lista[0] = 'Piccolo' #Altera o primeiro elemento da lista para 'Piccolo'
print(lista) #['Piccolo', 'Goku', 'Vegeta', 'Trunks', 'Gohan', 'Bulma']

#EXCLUIR ELEMENTOS DA LISTA
del lista [0] #Remove pelo indice, nesse caso o primeiro elemento
lista.remove('Bulma') #Remove pelo valor, nesse caso 'Bulma'
print(lista) #['Goku', 'Vegeta', 'Trunks', 'Gohan']

#ORDENAR ELEMENTOS DA LISTA
sorted_lista = sorted(lista) #Ordena a lista em ordem alfabética, mas não altera a lista original
lista.sort() #Ordena a lista em ordem alfabética e altera a lista original
lista.sort(reverse=True) #Inverte a ordem da lista
#esses ultimos são metódos de listas, ou seja, são funções que só funcionam com listas, já o sorted() é uma função do python


#EXEMPLOS DE CONJUNTOS {}
#Não gurada ordenação dos elementos, não permite elementos duplicados e é mutável
#Conjuntos são úteis quando você precisa garantir que não haja duplicatas e não se importa com a ordem dos elementos.
conjunto = {'Goku', 'Vegeta', 'Trunks', 'Gohan'}

#MOSTRANDO ELEMENTOS DO CONJUNTO
print(conjunto) #Mostra os elementos do conjunto, porém a ordem não é garantida, pois conjuntos não são ordenados

#ADICIONAR ELEMENTOS NO CONJUNTO
conjunto.add('Bulma') #Adiciona 'Bulma' no conjunto
conjunto.add('Goku') #Tentar adicionar 'Goku' novamente não vai fazer nada, pois conjuntos não permitem elementos duplicados
#conjuntos não permitem elementos duplicados, então se você tentar adicionar um elemento que já existe, ele não será adicionado novamente
#conjuntos são mutáveis, ou seja, podem ser alterados, mas os elementos dentro deles são imutáveis, ou seja, não podem ser alterados
print(conjunto) #Mostra os elementos do conjunto com 'Bulma' adicionado

#REMOVER ELEMENTOS DO CONJUNTO
conjunto.remove('Trunks') #Remove 'Trunks' do conjunto
print(conjunto) #Mostra os elementos do conjunto com 'Trunks' removido

#TROCAR ELEMENTOS DO CONJUNTO
#Não é possível trocar elementos de um conjunto, pois conjuntos não possuem índices,
#mas você pode remover um elemento e adicionar outro

#COMO DESCOBRIR O TIPO DE ALGO EM PYTHON?
print(type(conjunto)) #Mostra o tipo do objeto, nesse caso <class 'set'> para conjuntos


#EXEMPLOS DE DICIONÁRIOS {}
#Dicionários são coleções de pares chave-valor, onde cada chave é única e mapeada para um valor. 
#key:value
#chave:valor
pessoa = {
            'nome': 'Goku',
            'idade': 43,
            'sexo': 'Masculino',
            'planeta': 'Terra'
        }

#ADICIONAR ELEMENTOS NO DICIONÁRIO
pessoa['raca'] = 'Saiyajin' #Adiciona uma nova chave 'raça' com o valor 'Saiyajin'
pessoa['familia'] = ['Goten', 'Gohan','Chichi', 'Pan'] #Adiciona uma nova chave 'filhos' com o valor de uma lista contendo 'Goten' e 'Pan'

#ALTERAR ELEMENTOS DO DICIONÁRIO
pessoa['idade'] = 44 #Altera o valor da chave 'idade' para 44

#REMOVER ELEMENTOS DO DICIONÁRIO
del pessoa['sexo'] #Remove a chave 'sexo' do dicionário
#OBSERVAÇÃO: Dicionários são mutáveis, ou seja, podem ser alterados, mas as chaves são imutáveis, ou seja, não podem ser alteradas

#MOSTRANDO ELEMENTOS DO DICIONÁRIO
print(pessoa) #Mostra o dicionário completo
print(pessoa['familia'][2]) #Mostra o terceiro elemento da lista 'familia', que é 'Chichi'

