import random

numero_sorteado = random.randint(1, 100)

while True:
    palpite = int(input("Digite seu palpite: "))

    if palpite > numero_sorteado:
        print("tente um número menor.")
    elif palpite < numero_sorteado:
        print("tente um número maior.")
    else:
        print("você acertou")
        break