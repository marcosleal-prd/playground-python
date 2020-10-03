# Variaveis Compostas: Listas II
teste = list()
teste.append("Gustavo")
teste.append(40)

galera = list()
galera.append(teste[:])  # O [:] é necessário para evitar a referência

teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])

print(galera)
del teste
del galera

# Estrutura composta
galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
print(f"\n{galera}\n")

maiores = menores = 0
for pessoa in galera:
    if pessoa[1] >= 18:
        print(f"{pessoa[0]} é MAIOR de idade.")
        maiores += 1
    else:
        print(f"{pessoa[0]} é MENOR de idade.")
        menores += 1

print(f"\nMAIORES DE IDADE: {maiores}")
print(f"MENORES DE IDADE: {menores}")

galera.clear()
print(f"\nLISTA LIMPA: {galera}")
