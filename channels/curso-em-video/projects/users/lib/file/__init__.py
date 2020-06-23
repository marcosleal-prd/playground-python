from lib.interface import *

def fileExists(fileName):
    try:
        a = open(fileName, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def makeFile(fileName):
    try:
        a = open(fileName, 'wt+')
        a.close()
    except:
        print('\033[31mERRO: Não foi possível criar o arquivo!\033[m')
    else:
        print(f'\033[32mArquivo {name} criado com sucesso!\033[m')


def readFile(fileName):
    try:
        a = open(fileName, 'rt')
    except:
        print(f'\033[31mERRO: Não foi possível ler o arquivo!\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for line in a:
            dado = line.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()


def register(fileName, name='Desconhecido', age=18):
    try:
        a = open(fileName, 'at')
    except:
        print(f'\033[31mERRO: Não foi possível abrir a base de dados.\033[m')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print(f'\033[31mERRO: Não foi possível inserir o novo usuário.\033[m')
        else:
            print(f'\033[32mUsuário {name} cadastrado com sucesso!\033[m')
            a.close()

