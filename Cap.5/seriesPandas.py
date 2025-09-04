import pandas as pd

#PANDAS SERIES
#Array unidimensional
#Formada por dois elementos: indices (se não for setado automaticamente será um númerico) e valores

indices = ['a', 'b', 'c']
valores = [1,2,3]
dic = {'a':10, 'b':20, 'c':30}
dic2 = {'a':10, 'b':20, 'd':40}

#Criando e Mostrando a Series
#series = pd.Series(index=indices, data=valores)
series = pd.Series(dic)
series2 = pd.Series(dic2)
print(series)
print(type(series))
print(series['a']) #Acessando valor pelo indice

#Operações com Series
print(series + series2) #Soma os valores que possuem o mesmo indice, se não possuir o valor vira NaN (Not a Number)
print(series - series2) #Subtração
print(series * series2) #Multiplicação
print(series / series2) #Divisão

print(series.add(series2, fill_value=0)) #Soma, mas onde não tiver valor em uma das series, considera 0 ao invés de NaN
print(series.sub(series2, fill_value=0)) #Subtração

#CONDICIONAIS
print(series[series <=20])