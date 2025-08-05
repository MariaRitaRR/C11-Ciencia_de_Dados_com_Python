#  Faça um programa que leia um número entre 1000 e 9999 e mostre na tela 
# • qual o número da unidade
#  • número da dezena
#  • número da centena
#  • E número do milhar

numero = int(input("Digite um número entre 1000 e 9999: "))
if 1000 <= numero <= 9999:
    unidade = numero % 10
    dezena = (numero // 10) % 10
    centena = (numero // 100) % 10
    milhar = (numero // 1000) % 10
    
    print(f"Número: {numero}")
    print(f"Unidade: {unidade}")
    print(f"Dezena: {dezena}")
    print(f"Centena: {centena}")
    print(f"Milhar: {milhar}")