preco = float(input("Digite o preço do produto: "))
desconto = 5 / 100

preco_com_desconto = preco - (preco * desconto)

print(f"O preço com desconto de {desconto * 100:.0f}% é: {preco_com_desconto}")
