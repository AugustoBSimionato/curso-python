import math

catetoOposto = float(input("Digite o cateto oposto: "))
catetoAdjacente = float(input("Digite o cateto adjacente: "))

hipotenusa = math.sqrt(catetoOposto**2 + catetoAdjacente**2)

print(f"A hipotenusa é {hipotenusa:.2f}")
