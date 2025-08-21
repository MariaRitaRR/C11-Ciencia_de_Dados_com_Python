#  2. Crie dois NumPy Arrays unidimensionais: um de números pares de 0 à 51 e 
# outro também de números pares de 100 até 50. Em seguida, os concatene e 
# mostre os resultados ordenados

import numpy as np

arr1 = np.arange(0, 52, 2) 
arr2 = np.arange(100, 48, -2)

arr3 =np.concatenate((arr1, arr2))
arr3_sorted = np.sort(arr3)

print("Array Concatenado e Ordenado:", arr3_sorted)

