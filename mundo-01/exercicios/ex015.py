kmPercorridos = float(input("Digite a quantidade de km percorridos: "))
diasAlugado = int(input("Digite a quantidade de dias alugados: "))

carro = 60
kmRodado = 0.15

valorTotal = (diasAlugado * carro) + (kmPercorridos * kmRodado)

print(f"O valor total a ser pago é: R$ {valorTotal:.2f}")
