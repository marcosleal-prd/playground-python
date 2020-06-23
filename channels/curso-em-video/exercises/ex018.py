# Funcoes I
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'Soma de A + B = {s}')


soma(6, 2)
soma(b=3, a=1)
print()

'''
IMPORTANTE!!!
Entre qualquer def e a próxima linha de código, deve sempre haver no mínimo 2
linhas em branco de espaçamento.
'''

# Numero de Parametros (Empacotamento)
def contador(*num):
    print(f'CONTADOR: {num}')


contador(1, 4, 5, 2)
contador(2, 10)
contador(9, 3, 46, 198, 2, 0, 1)

# Parametros (Listas)
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [1, 7, 3, 4, 11]
dobra(valores)
print(f'\nVALORES DOBRADOS: {valores}')

