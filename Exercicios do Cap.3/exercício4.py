# 4. Faça um programa que leia o nome e peso de 3 pessoas e no final 
# mostre o nome da pessoa mais pesada e a mais leve


pessoas = {}

for i in range(3):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    peso = float(input(f"Digite o peso de {nome} (em kg): "))
    pessoas[nome] = peso

mais_leve = min(pessoas, key=pessoas.get)
mais_pesada = max(pessoas, key=pessoas.get) 

print(f"A pessoa mais leve é {mais_leve} com {pessoas[mais_leve]} kg.")
print(f"A pessoa mais pesada é {mais_pesada} com {pessoas[mais_pesada]} kg.")