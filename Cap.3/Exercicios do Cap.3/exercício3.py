#  Faça um programa que leia o nome e a média de um aluno e guarde
# os em um dicionário. Em seguida, a partir da média (para ser 
# aprovado deve ter média >=50), gere a situação final do aluno (‘AP’ 
# ou ‘RP’), que  também deve ser guardada neste dicionário. No final, 
#  mostre todo o conteúdo deste dicionário;

aluno = {}
aluno['nome'] = input("Digite o nome do aluno: ")
aluno['media'] = float(input("Digite a média do aluno: "))
if aluno['media'] >= 50:
    aluno['situacao'] = 'AP'  # Aprovado
else:
    aluno['situacao'] = 'RP' # Reprovado

print("Dados do aluno:")
print("Nome:", aluno['nome'])
print("Média:", aluno['media'])
print("Situação:", aluno['situacao'])  # Mostra a situação final do aluno