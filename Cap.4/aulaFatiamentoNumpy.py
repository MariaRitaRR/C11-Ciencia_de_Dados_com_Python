#SLICING EM NUMPY ARRAYS
import numpy as np

# Criando um array 2D
mtz = np.arange(1,10,1).reshape(3,3)
print (mtz)


# EXTRAINDO APENAS UMA LINHA
print(mtz[2]) # Exibe a terceira linha do array

#EXTRAINDO APENAS UMA COLUNA
print(mtz[:,1]) # Exibe a segunda coluna do array

print(mtz[:,1:]) # Exibe da primeira coluna para a frente

#CONDICIONAIS NO NUMPY ARRAY
print(mtz>5) # Exibe um array booleano com True onde o valor é maior que 5
print(mtz[mtz>5]) # Exibe os valores do array que são maiores que 5
print(mtz[mtz%2==0]) # Exibe os valores do array que são pares


#TRATAMENTO TEXTUAL (Subpacote char)
arr = np.array(['Bloom', 'Stela', 'Flora', 'Musa', 'Aisha','Luna'])
arr = np.char.upper(arr) # Converte todas as strings do array para maiúsculas
print(arr)
print(np.char.find(arr,'L')) # Encontra a letra 'l' em cada string do array
print(np.char.find(arr,'L') >= 0) # Verifica se a letra 'l' está presente em cada string do array
print(arr[np.char.find(arr,'L') >= 0]) # Exibe as strings que contêm a letra 'l'

