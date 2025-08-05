# Peça ao usuário para entrar com um número decimal. Em seguida, aplique e mostre o resultado: 
# • da raiz quadrada deste número
# • função teto
# • função chão
# • sua parte inteira

import math
numero = float(input("Digite um número decimal: "))
raiz_quadrada = math.sqrt(numero)
teto = math.ceil(numero)
chao = math.floor(numero)
parte_inteira = int(numero)
print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}.")
print(f"O teto de {numero} é {teto}.")
print(f"O chão de {numero} é {chao}.")
print(f"A parte inteira de {numero} é {parte_inteira}.")
