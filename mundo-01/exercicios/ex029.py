velocidade = float(input("Digite a velocidade: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você ultrapassou a velocidade permitida. E foi multado em: R${multa:.2f} reais")
print("Você está dentro da velocidade permitida.")
