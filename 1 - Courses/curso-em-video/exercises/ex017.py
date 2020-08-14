# Variaveis Compostas: Dicionarios
pessoa = { 'nome': 'Marcos', 'idade': 23, 'sexo': 'M' }
print(f'CHAVES: {pessoa.keys()}')
print(f'VALORES: {pessoa.values()}')
print(f'ITEMS: {pessoa.items()}\n')

for k in pessoa.keys():
    print(f'CHAVE ATUAL: {k}')

for v in pessoa.values():
    print(f'VALOR ATUAL: {v}')

for k, v in pessoa.items():
    print(f'CHAVE {k} TEM VALOR {v}')

# Referencia
series = []
serie1 = { 'nome': 'House Of Cards', 'canal': 'Netflix' }
serie2 = { 'nome': 'Suits', 'canal': 'Netflix' }

series.append(serie1)
series.append(serie2)
print(f'\nSÉRIE 1: {serie1}')
print(f'SÉRIE 2: {serie2}')
print(f'SUAS SÉRIES: {series}')

serie2['nome'] = 'Friends'
print(f'\nSÉRIE 1: {serie1}')
print(f'SÉRIE 2: {serie2}')
print(f'SUAS SÉRIES: {series}')

'''
Novamente a atribuição simples de uma variável composta á outra gera uma
ligação por referência, ou seja, quando o valor da variável original for
alterado o mesmo afetará a variável que recebe a atribuição.

No caso dos discionários, para evitar a refência deve-se utilizar o método
.copy(). Veja o mesmo exemplo abaixo, mas note a diferênça no campo 'nome'.
'''
series.pop()
series.append(serie2.copy())
serie2['nome'] = 'Flash'

print(f'\nSÉRIE 1: {serie1}')
print(f'SÉRIE 2: {serie2}')
print(f'SUAS SÉRIES: {series}')

