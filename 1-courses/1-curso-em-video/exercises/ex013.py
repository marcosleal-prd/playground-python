# Estrutura de Repeticao: While

r = "S"
while r == "S":
    v = int(input("Digite um valor: "))
    r = str(input("Quer continuar? [S/N] ")).upper()
print("--FIM--")

n = 1
par = impar = 0
while True:
    n = int(input("Digite um número: "))
    if n == 0:
        break

    if n % 2 == 0:
        par += 1
    else:
        impar += 1

print("Você digitou {} pares e {} ímpares!".format(par, impar))
