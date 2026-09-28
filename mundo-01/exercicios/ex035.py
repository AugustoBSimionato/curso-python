reta1 = float(input("Digite o comprimento da reta 1: "))
reta2 = float(input("Digite o comprimento da reta 2: "))
reta3 = float(input("Digite o comprimento da reta 3: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("As retas podem formar um triângulo.")
else:
    print("As retas não podem formar um triângulo.")
