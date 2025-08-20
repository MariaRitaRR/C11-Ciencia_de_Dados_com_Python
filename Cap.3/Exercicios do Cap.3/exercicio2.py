# Crie dois conjuntos, um para cada loja. Identifique quais modelos de 
# smartphones cada uma delas vendem. Em seguida, mostre quais 
# modelos no total você terá opção de comprar se visita-las e quais 
# modelos se encontram disponíveis em ambas as lojas

loja1 = {'iPhone 14', 'Samsung Galaxy S22', 'Google Pixel 6'}
loja2 = {'Samsung Galaxy S22', 'Google Pixel 6', 'OnePlus 9'}

print("Modelos disponíveis na Loja 1:", loja1)
print("Modelos disponíveis na Loja 2:", loja2)

# Modelos disponíveis em ambas as lojas
modelos_em_ambas = loja1.intersection(loja2)
print("Modelos disponíveis em ambas as lojas:", modelos_em_ambas)