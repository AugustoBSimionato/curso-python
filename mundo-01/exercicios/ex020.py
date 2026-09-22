from random import shuffle

primeiroNome = input("Digite o primeiro nome: ")
segundoNome = input("Digite o segundo nome: ")
terceiroNome = input("Digite o terceiro nome: ")
quartoNome = input("Digite o quarto nome: ")

nomes = [primeiroNome, segundoNome, terceiroNome, quartoNome]

shuffle(nomes)
print(f"Ordem da apresentação: {nomes}")
