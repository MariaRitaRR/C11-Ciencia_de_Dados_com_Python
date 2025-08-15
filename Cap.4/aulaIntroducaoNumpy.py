#CRIANDO NUMPY ARRAYS
import numpy as np  #as  da um apelido mais curto

arr = np.array([10, 20, 30])  #Array é uma classe do numpy

print(arr)  #Exibe o array criado
print(type(arr))  #Exibe o tipo do objeto arr

mtz = np.array([[1, 2, 3], [4, 5, 6]])  #Matriz é um array de duas dimensões
print(mtz)  #Exibe a matriz criada

#FUNÇÕES PARA ESTRUTURAR ARRAYS
#array 1D de 1s
arr1 = np.ones(10) #Cria um array de 1 dimensão com 10 elementos, todos iguais a 1
print(arr1)

#Array 2D de 0s com reshape
mtz1 = np.zeros(10).reshape(5,2) #Cria um array de 2 dimensões com 10 elementos, todos iguais a 0
print(mtz1)

mtz2 = np.zeros([5,2])  #Cria um array de 2 dimensões com valores de 0

#ARANGE
arr2 = np.arange(10 ,101, 10) #Cria um array de 1 dimensão com valores de 10 a 100, com passo de 10
print(arr2)
#menor valor
print(arr2.min())  #Exibe o menor valor do array
#maior valor
print(arr2.max())  #Exibe o maior valor do array
#indice do menor valor
print(arr2.argmin())  #Exibe o índice do menor valor do array
#indice do maior valor
print(arr2.argmax())  #Exibe o índice do maior valor do array


#OPERAÇÕES COM ARRAYS
arr3 = np.arange(1 , 10, 1)  #Cria um array de 1 dimensão com valores de 1 a 10
arr4 = np.arange(9, 0, -1)  #Cria um array de 1 dimensão com valores de 9 a 0, com passo de -1
print(arr3)
print(arr4)

#Soma dos arrays
print(arr3 + arr4)  #Soma elemento a elemento dos dois arrays
#Subtração dos arrays
print(arr3 - arr4)  #Subtrai elemento a elemento dos dois arrays
#Multiplicação dos arrays
print(arr3 * arr4)  #Multiplica elemento a elemento dos dois arrays
#Divisão dos arrays
print(arr3 / arr4)  #Divide elemento a elemento dos dois arrays
#Divisão inteira dos arrays
print(arr3 // arr4)  #Divisão inteira elemento a elemento dos dois arrays
#Módulo dos arrays
print(arr3 % arr4)  #Módulo elemento a elemento dos dois arrays
#Potência dos arrays
print(arr3 ** arr4)  #Eleva elemento a elemento do primeiro array ao valor correspondente do segundo array
#Media dos arrays
print((arr3 + arr4) / 2)  #Calcula a média elemento a elemento dos dois arrays
# #Comparação dos arrays
print(arr3 == arr4)  #Compara elemento a elemento dos dois arrays, retornando um array booleano
print(arr3 > arr4)  #Compara elemento a elemento dos dois arrays, retornando um array booleano
print(arr3 < arr4)  #Compara elemento a elemento dos dois arrays, retornando um array booleano

#os elementos dos arrays devem ser do mesmo tamanho para realizar operações entre eles
#Caso contrário, ocorrerá um erro de broadcasting
#Broadcasting é a capacidade do numpy de realizar operações entre arrays de tamanhos diferentes
#O numpy tenta ajustar os arrays para que possam ser operados entre si
#Por exemplo, se um array for 1D e o outro for 2D,
#o numpy tentará ajustar o array 1D para que ele possa ser operado com o array 2D
#Isso pode levar a resultados inesperados, por isso é importante ter cuidado com o tamanho dos arrays
#Se os arrays não puderem ser ajustados, ocorrerá um erro de broadcasting
#Por exemplo, se um array for 1D com 3 elementos
#e o outro for 2D com 2 linhas e 3 colunas, o numpy não conseguirá ajustar os arrays
#e ocorrerá um erro de broadcasting

#CONCATENAÇÃO DE ARRAYS
#Concatenar arrays significa unir dois ou mais arrays em um único array
print(np.concatenate((arr3, arr4)))  #Concatena os dois arrays em um único array

#OPRERAÇÕES COM MATRIZES

mtz3 = np.array([50,10,100,60,25,100,75,80,100]).reshape(3,3)  #Cria uma matriz de 3 linhas e 3 colunas
print(mtz3)  #Exibe a matriz criada

print(mtz3.sum())  #Soma todos os elementos da matriz
print(mtz3.sum(axis=0))  #Soma os elementos da matriz ao longo do eixo 0 (colunas)
print(mtz3.sum(axis=1))  #Soma os elementos da matriz ao longo do eixo 1 (linhas)
print(mtz3.sum(axis=0)[2])  #Soma dos elementos da terceira coluna da matriz

print(mtz3.mean())  #Média de todos os elementos da matriz
print(mtz3.mean(axis=0))  #Média dos elementos da matriz ao longo do eixo 0 (colunas)
print(mtz3.mean(axis=1))  #Média dos elementos da matriz ao longo do eixo 1 (linhas)

#BROADCASTING
#possibilita a opreação entre um escalar e um array
print(mtz3/10)  #Divide todos os elementos da matriz por 10


#NÚMEROS ALEATÓRIOS
arr5 = np.random.randint(1, 101, 10)  #Cria um array de 1 dimensão com 10 elementos aleatórios entre 1 e 100
print(arr5)  #Exibe o array criado

#SEED ALEATÓRIO
np.random.seed(10)  #Define uma semente para os números aleatórios, garantindo
arr6 = np.random.randint(1, 10, 10)  #Cria um array de 1 dimensão com 10 elementos aleatórios entre 1 e 100
print(arr6)  #Exibe o array criado com a semente definida
print(np.unique(arr6))  #Exibe os valores únicos do array, removendo duplicatas
print(np.unique(arr6, return_counts=True))  #Exibe os valores únicos do array e suas contagens
