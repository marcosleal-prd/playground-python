# Funcoes II

# DOCSTRINGS
def contador(i,f,p):
    """
        -> Faz uma contagem e mostra na tela.
        :param i: início da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}...')
        c += p


contador(2, 10, 2) # help(contador)
print()

# Parametros Opcionais
def somar(a, b, c=0):
    print(a, b, c)
    s = a + b + c
    print(f'A SOMA DOS VALORES É: {s}')


somar(3, 2, 5)
somar(3, 2)

# Escopo de variaveis
print()
def scope():
    x = 8
    print(f'NA FUNÇÃO SCOPE, N VALE: {n}')
    print(f'NA FUNÇÃO SCOPE, X VALE: {x}')


n = 2
print(f'NO PROGRAMA PRINCIPAL, N VALE: {n}')
scope()
'''
print(f'NO PROGRAMA PRINCIPAL, X VALE: {x}') - linha com erro, x tem escopo local.

O cenário abaixo ilustra o efeito do escopo de variaveis, nele a variavel local  n1
(n1 = 9) não sobreescreve a variável global n1 com valor inicial 0. Neste
contexto haverão 2 variáveis n1, uma local com valor 8 e uma global com valor
0.
'''

print()
def func():
    n1 = 8
    print(f'N1 dentro vale: {n1}')


n1 = 0
func()
print(f'N1 fora vale: {n1}')

'''
Para utilizar uma variavel global dentro do escopo de uma funcao sem que isso
crie uma variavel local de mesmo nome, deve-se utilizar o `global` antes da
atribuicao do novo valor dentro da funcao. Veja abaixo:
'''
print()
def funcGlobal():
    global n2
    n2 = 8
    print(f'N2 dentro vale: {n2}')


n2 = 0
funcGlobal() # essa chamada deve sobreescrever n2 com 8
print(f'N2 fora vale: {n2}\n')

# Retorno de valores
def multiplica(a, b):
    return a * b


result1 = multiplica(2, 5)
result2 = multiplica(3, 9)
print(f'RESULT 1: {result1}')
print(f'RESULT 2: {result2}')

