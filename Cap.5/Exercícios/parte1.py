import pandas as pd

#1 Crie duas Series com os seguintes valores
# seriesAno 1 :{‘ 16 25 ,,‘ 16 04 ,,‘ 9 85}
# seriesAno 2 :{‘ 16 21 ,,‘ 12 12 ,,‘ 11 68}
dicAno1 =  {'Java': 16.25, 'C': 16.04, 'Python': 9.85}
dicAno2 = {'C':16.21 , 'Python': 12.12, 'Java': 11.68}

seriesAno1 = pd.Series(dicAno1)
seriesAno2 = pd.Series(dicAno2)


2
# Os valores das Series criadas na Questão 1 representam as fatias de mercado de 3 linguagens de programação populares em
# dois anos consecutivos Para cada ano, apresente a porcentagem total que elas juntas representam no mercado
somaAno1 = seriesAno1.sum()
somaAno2 = seriesAno2.sum()

print(f"Porcentagem total ano 1: {somaAno1}% \nPorcentagem total ano 2: {somaAno2}%")

# 3 Apresente o crescimento/declínio no mercado de cada linguagem do primeiro ano para o segundo ano
crescimento = seriesAno2 - seriesAno1
for i in range(len(crescimento)):
    if crescimento.iloc[i] > 0:
        print(f"\nA linguagem {crescimento.index[i]} teve um crescimento de {crescimento.iloc[i]:.2f}%")
    else:
        print(f"\nA linguagem {crescimento.index[i]} teve um declínio de {abs(crescimento.iloc[i]):.2f}%")

# 4 Baseado nos resultados da Questão 3 mostre apenas os dados das linguagens que tiveram crescimento

for i in range(len(crescimento)):
    if crescimento.iloc[i] > 0:
        print(f"\nA linguagem {crescimento.index[i]}:\n no primeiro ano teve {seriesAno1[crescimento.index[i]]}% \n no segundo ano teve {seriesAno2[crescimento.index[i]]}% \n teve um crescimento de {crescimento.iloc[i]:.2f}%\n")

# 5 Se estas porcentagens de crescimento/declínio se mantivessem iguais para os próximos 2 anos, qual seria a linguagem mais popular?
# Dica : use o método nlargest 1 no final para retornar rapidamente a labele maior valor de uma Series

linguagemMaisPopular = seriesAno2 + (crescimento * 2)
print(f"Linguagem mais popular daqui dois anos:{linguagemMaisPopular.nlargest(1)}")

