from random import choice

primeiroNome = input("Digite o primeiro nome: ")
segundoNome = input("Digite o segundo nome: ")
terceiroNome = input("Digite o terceiro nome: ")
quartoNome = input("Digite o quarto nome: ")

sorteado = choice([primeiroNome, segundoNome, terceiroNome, quartoNome])

print(f"O nome sorteado é: {sorteado}")
