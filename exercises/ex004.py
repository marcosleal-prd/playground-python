# -*- coding: UTF-8 -*-
a = input('Digite algo: ')

print('Valor bruto: {}'.format(a))
print('Tipo do valor: {}', type(a))
print('É apenas espaços: ', a.isspace())
print('É um número: ', a.isnumeric())
print('É alfabético: ', a.isalpha())
print('É alfanumérico: ', a.isalnum())
print('Está em maiúsculo? ', a.isupper())
print('Está em minúsculo? ', a.islower())
print('Está capitalizado? ', a.istitle())
