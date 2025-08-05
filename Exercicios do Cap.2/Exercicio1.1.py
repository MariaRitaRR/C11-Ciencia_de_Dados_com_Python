# Crie um programa que leia seu nome completo e mostre:
# Seu nome com todas as letras maiúsculas
# Seu nome com todas as letras minúsculas
# Quantas letras ao todo tem seu nome
# E como seria se trocássemos seu último nome para “do Inatel”

nome = input("Digite seu nome completo: ")
print("Seu nome em maiúsculas:", nome.upper())
print("Seu nome em minúsculas:", nome.lower())
print("Seu nome tem", len(nome.replace(" ", "")), "letras ao todo.")
ultimo_nome = nome.split()[-1]
novo_nome = nome.replace(ultimo_nome, "do Inatel")
print("Seu nome com o último nome trocado:", novo_nome) 