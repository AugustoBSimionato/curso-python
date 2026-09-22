nomeCompleto = input('Digite seu nome completo: ')

print(f"Maiusculo: {nomeCompleto.upper()}")
print(f"Minusculo: {nomeCompleto.lower()}")

print(f"Letras ao todo (sem contar espaços): {len(nomeCompleto.replace(' ', ''))}")

primeiroNome = nomeCompleto.split()[0]
print(f"Quantidade de letras do primeiro nome: {len(primeiroNome)}")
