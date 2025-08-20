# Crie uma lista preenchida com os 5 primeiros colocados de um 
# Campeonato de Futebol, na ordem de colocação. Depois mostre:

#  Apenas os 3 primeiros colocados;
#  Os últimos 2 colocados;
#  Uma lista com os times em ordem alfabética;
#  Em que posição da tabela se encontra o Barcelona

campeonato = ['Corinthians', 'Palmeiras', 'Santos', 'São Paulo', 'Barcelona']
print("Os 3 primeiros colocados:", campeonato[:3])  # Apenas os 3 primeiros colocados
print("Os últimos 2 colocados:", campeonato[-2:])  # Os últimos 2 colocados
print("Times em ordem alfabética:", sorted(campeonato))  # Lista com os times em ordem alfabética
print("O Barcelona está na posição:", campeonato.index('Barcelona') + 1)  # Posição do Barcelona (índice + 1 para ajustar à contagem humana)

