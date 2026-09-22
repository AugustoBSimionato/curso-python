import math

angulo = float(input("Digite o ângulo: "))

seno = math.sin(math.radians(angulo))
print(f"O seno é {seno:.2f}")

coseno = math.cos(math.radians(angulo))
print(f"O cosseno é {coseno:.2f}")

tangente = math.tan(math.radians(angulo))
print(f"A tangente é {tangente:.2f}")
