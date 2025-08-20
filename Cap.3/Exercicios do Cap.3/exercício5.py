#  5. Desenvolva um programa que leia o nome, idade e sexo de n pessoas. 
# No final, mostre:
#  A média de idade do grupo;
#  Quantas mulheres têm menos de 20 anos

pessoas = []
soma_idade = 0
num_mulheres_menor_20 = 0
n = int(input("Quantas pessoas deseja cadastrar? "))
for i in range(n):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    sexo = input(f"Digite o sexo de {nome} (M/F): ").strip().upper()
    
    pessoas.append({'nome': nome, 'idade': idade, 'sexo': sexo})
    soma_idade += idade
    
    if sexo == 'F' and idade < 20:
        num_mulheres_menor_20 += 1

media_idade = soma_idade / n if n > 0 else 0
print(f"A média de idade do grupo é: {media_idade:.2f} anos")
print(f"Quantidade de mulheres com menos de 20 anos: {num_mulheres_menor_20}") 