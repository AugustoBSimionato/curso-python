distancia = float(input("Digite a distância em km: "))

if distancia <= 200:
    preco = 0.50
    valorPassagem = preco * distancia
else:
    preco = 0.45
    valorPassagem = preco * distancia

print(f"O valor da passagem é R$ {valorPassagem:.2f}.")
