#  3. Mini Campo Minado
#  Crie um NumPy Array 2x2 formado apenas por 0’s
#  Em seguida, adicione um número 1 em uma posição aleatória desta matriz;
#  Faça uma entrada de dados para solicitar o usuário que faça uma jogada
# (selecione uma posição da matriz)
#  Se ele selecionar todas as posições em que o número 1 não se encontra, mostre a
# mensagem “Congratulations! You beat the game! :)”
#  Senão, se dentro das 3 primeiras jogadas ele achar o número 1, mostre a mensagem
# “Game Over! :( Try Again!”)
import numpy as np
import random

campo_minado = np.zeros((2, 2), dtype=int)
random_x = random.randint(0, 1)
random_y = random.randint(0, 1)
campo_minado[random_x, random_y] = 1

print("Welcome to Mini Campo Minado!")
print("You have 3 attempts to find the hidden 1 in the 2x2 grid.")
print("The grid positions are as follows:")
print(" (0,0) (0,1) ")
print(" (1,0) (1,1) ")

for tentativa in range(3):
        x = int(input("Enter the row (0 or 1): "))
        y = int(input("Enter the column (0 or 1): "))
        if campo_minado[x, y] == 1:
            print("Game Over! :( Try Again!")
            op = 0
            break
        else:
            print("No mine here! Try again.")
        if tentativa == 2:
            print ("Congratulations! You beat the game! :)")
        




