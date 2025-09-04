import numpy as np

ds = np.loadtxt('paises.csv',
                delimiter=';',
                dtype=str,
                encoding='utf-8')

#Faça um slicing no dataset para mostrar apenas o País (Country), Região (Region), População (Population) e Area (Area (sq. mi.)) dos países contidos nele;
ds_1 = ds[1:,0:4]
print(ds_1)

#Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo este dataset; 
regiao = ds[1:,1]
cont_regiao,cont = np.unique(regiao,return_counts=True)
for i in range(len(cont_regiao)):
    print(f'Região: {cont_regiao[i]} - Quantidade de países: {cont[i]}')

#Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo este dataset;
alfabetização = ds[1:,9].astype(float)
media_alfabetizacao = np.mean(alfabetização)
print(f'Media de alfabetização: {media_alfabetizacao:.2f}%')

#Conte quantos países são da América do Norte (NORTHERN AMERICA) segundo este dataset;
regiao = np.char.strip(ds[1:,1])
america_do_norte = regiao == 'NORTHERN AMERICA'
print(f'Países da América do Norte: {len(america_do_norte)}')

#Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB) possui a maior renda per capita (GDP ($ per capita));
latin_carib_mask = np.char.strip(ds[1:,1] )== 'LATIN AMER. & CARIB'
latin_carib_data = ds[1:][latin_carib_mask]

gpd_valores = latin_carib_data[:,8].astype(float)
indice_maior = np.argmax(gpd_valores)
pais = latin_carib_data[indice_maior,0]
maior_gpd = gpd_valores[indice_maior]
print(f'País com maior GDP na América do Sul e Caribe: {pais} com GDP de {maior_gpd}')