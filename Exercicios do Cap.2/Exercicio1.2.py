# Mostre a tabuada de um número que o usuário escolher dentro de um intervalo específico também escolhido por ele

numero = int(input("Digite um número para ver sua tabuada: "))
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

print(f'Tabuada do nímero {numero} de {inicio} a {fim}: ')
for i in range(inicio, fim + 1):
    print(f'{numero} x {i} = {numero * i}')