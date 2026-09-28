salario = float(input("Digite o salário: "))

if salario > 1250:
    novoSalario = salario + (salario * 0.1)
    print(f"O novo salário é: {novoSalario}")
elif salario <= 1250:
    novoSalario = salario + (salario * 0.15)
    print(f"O novo salário é: {novoSalario}")
