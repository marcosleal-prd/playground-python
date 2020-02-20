from lib.interface import *

opcoes = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema']
while True:
    resposta = menu(opcoes)
    if resposta == 1:
        print('Opcao 1')
    elif resposta == 2:
        print('Opcao 2')
    elif resposta == 3:
        print('Saindo do sistema...')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida!\033[m')

