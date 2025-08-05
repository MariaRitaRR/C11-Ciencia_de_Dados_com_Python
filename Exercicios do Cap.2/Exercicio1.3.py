#  Faça um programa que leia o sexo de uma pessoa e diga se ela é homem (caso seja digitado M) ou mulher (caso seja digitado F). 
# Caso seja digitado algo inválido, continue perguntando até que o usuário entre com um sexo válido

sexo = input("Digite o sexo (M para homem, F para mulher): ").strip().upper()
while sexo not in ['M', 'F']:
    print("Sexo inválido. Por favor, digite M para homem ou F para mulher.")
    sexo = input("Digite o sexo (M para homem, F para mulher): ").strip().upper()
if sexo == 'M':
    print("Você é homem.")
else:
    print("Você é mulher.")