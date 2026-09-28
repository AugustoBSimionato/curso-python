import random

print("Pensando em um número...")

num = random.randint(0, 5)

usuario = int(input("Digite um número entre 0 e 5: "))

if usuario == num:
    print("Parabéns! Você acertou.")
else:
    print(f"Você errou. O número pensado foi {num}.")
