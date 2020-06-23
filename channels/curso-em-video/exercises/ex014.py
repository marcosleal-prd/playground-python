# Variaveis Compostas: Tuplas
# Tuplas São Imutáveis

# Parenteses são opcionais
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

# print('LANCHES: ', lanche)
# print('TOTAL DE LANCHES: ', len(lanche))
# print('HAMBURGUER: ', lanche[0])
# print('PUDIM: ', lanche[-1])
# print('SUCO E PIZZA: ', lanche[1:3])

# Apenas Valor
print('EXIBINDO APENAS VALOR:')
for c in lanche:
    print(f'Eu vou comer {c}!')

# Posicao e Valor
print('\nEXIBINDO POSICAO E VALOR I')
for pos in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[pos]} na posição {pos}')

# Posicao e Valor
print('\nEXIBINDO POSICAO E VALOR II')
for i, name in enumerate(lanche):
    print(f'Eu vou comer {name} na posição {i}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print('\nJUNÇÃO DE TUPLAS (ORDEM IMPORTA)')
print(f'Tupla C: {c}')
print(f'5 acontece {c.count(5)} vezes')
print(f'8 está na posição {c.index(8)}')
print(f'Onde está o número 5 ignorando a segunda posição? {c.index(5, 2)}')

# Remove Tupla
del(lanche)
print(lanche)
