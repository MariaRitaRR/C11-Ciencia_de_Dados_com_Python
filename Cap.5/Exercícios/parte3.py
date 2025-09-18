import pandas as pd

dfPaises = pd.read_csv('paises.csv', delimiter=';')

#1
#Quais são os paíeses da OCEANIA?
paises_oceania = dfPaises[dfPaises['Region'].str.contains('OCEANIA')]['Country']
print(paises_oceania)

#Quantos países são da OCEANIA?
num_paises_oceania = paises_oceania.count()
print(num_paises_oceania)

# País com maior 

maior_populacao = dfPaises.loc[dfPaises['Population'].idxmax()]
print(f"País com maior população: {maior_populacao['Country']}")
print(f"Região: {maior_populacao['Region']}")
print(f"População: {maior_populacao['Population']}")

# Média de alfabetização por região
media_alfabetizacao = dfPaises.groupby('Region')['Literacy (%)'].mean()
print(media_alfabetizacao)

# Países sem costa marítima e salvar em arquivo
paises_sem_costa = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]['Country']
paises_sem_costa.to_csv('paises_sem_costa.csv', index=False)


#Função para classificar taxa de mortalidade

def classificar_mortalidade(deathrate):
    if deathrate < 9:
        return 'Balanced'
    else:
        return 'Urgent'
    
dfPaises['Humaniarian Help'] = dfPaises['Deathrate'].apply(classificar_mortalidade)

print(dfPaises[['Country', 'Deathrate', 'Humaniarian Help']])