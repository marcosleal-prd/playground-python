# Estrutura Condicional I
tempo = int(input("Quantos anos tem seu carro? "))

# Modo 2 (Simplificada)
# print('Carro novo' if tempo <= 3 else 'Carro velho')

# Modo 1 (Recomendado)
if tempo <= 3:
    print("Carro novo")
else:
    print("Carro velho")

print("--FIM--")
