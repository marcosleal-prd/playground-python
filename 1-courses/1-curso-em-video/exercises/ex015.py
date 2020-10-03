# Variaveis Compostas: Listas I
numbers = list([2, 5, 9, 1])  # ou [2, 5, 9, 1] ou list()
numbers[2] = 3

# Total de elementos
print(f"ELEMENTOS NA LISTA: {len(numbers)}")

# Insercao de novos elementos
# numbers[4] = 7 (Isso não funciona no Python)
numbers.append(7)
print(f"DESORDENADA: {numbers}")

numbers.insert(2, 0)
print(f"LISTA APOS INSERT: {numbers}")

# Ordenacao
numbers.sort()
print(f"ORDENADA ASC: {numbers}")

numbers.sort(reverse=True)
print(f"ORDENADA DESC: {numbers}")

# Remocao de elementos
numbers.pop()
print(f"LISTA APOS POP: {numbers}")

numbers.pop(2)
print(f"LISTA APOS POP2: {numbers}")

numbers.insert(0, 2)
print(f"LISTA ANTES DO REMOVE: {numbers}")
if 2 in numbers:
    numbers.remove(2)  # remove APENAS a 1ª ocorrencia do valor buscado
print(f"LISTA APOS REMOVE: {numbers}")

# Percorrendo a lista
for i, v in enumerate(numbers):
    print(f"Posicao {i} com valor {v}")

list1 = [2, 4, 8]
list2 = list1
list2[1] = 17
print(f"LISTA 1 (LIGADA): {list1}")
print(f"LISTA 2 (LIGADA): {list2}")

"""
No Python ao igualar uma lista à outra (como no exemplo acima), qualquer
modificação realizada em uma delas terá reflexo direto na outra. Isso ocorre
porque essa igualdade gera o que é chamado de REFERÊNCIA, ou seja, ambas as
listas apotam para o mesmo espaço de memória.

Para criar uma cópia, deve-se utilizar o recurso de FATIAMENTO, como no exemplo
abaixo. Assim, todos os valores de uma lista serão atribuídos à outra lista em outro
espaço na memória.
"""

list2 = list1[:]
list2[1] = 23
print(f"LISTA 1 (COPIA): {list1}")
print(f"LISTA 2 (COPIA): {list2}")
