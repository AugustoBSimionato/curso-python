# nome = input('Digite seu nome: ')
# print(f'Prazer em te conhecer {nome:>20}!')

# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# print(f'A soma entre {n1} e {n2} é {n1 + n2}!')

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1**n2

print(
    f"A soma é {s}, \n o produto é {m}, \n a divisão é {d:.3f}, \n a divisão inteira é {di}, \n e o resto é {e}.", end = ' >>>> '
)
