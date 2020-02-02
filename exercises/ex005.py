# -*- coding: UTF-8 -*-

## Ordem de Precedência
# 1 ()
# 2 **
# 3 * / // %
# + -

# Operações com String
nome = input('Qual seu nome: ')
print('Prazer em te conhecer, {:20}!'.format(nome))
print('Prazer em te conhecer, {:>20}!'.format(nome))
print('Prazer em te conhecer, {:<20}!'.format(nome))
print('Prazer em te conhecer, {:^20}!'.format(nome))
print('Prazer em te conhecer, {:=^20}!'.format(nome))

# Operações Aritméticas
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A SOMA é: {}, o PRODUTO é: {}, e a DIVISÃO é {:.3f}'.format(s, m, d),
      end=' ')
print('A DIVISÃO INTEIRA é: {} e a POTÊNCIA é: {}.'.format(di, e))
