import random

numero_sorteado = random.randint(1, 100)

while True:
    palpite = int(input("Digite seu palpite: "))

    if palpite > numero_sorteado:
        print("Alto demais! Tente um número menor.")
    elif palpite < numero_sorteado:
        print("Baixo demais! Tente um número maior.")
    else:
        print("Parabéns, você acertou!")
        break