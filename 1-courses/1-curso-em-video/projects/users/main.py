from lib.interface import *
from lib.file import *
from time import sleep

database = "users-database.txt"
opcoes = ["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"]

if not fileExists(database):
    makeFile(database)

while True:
    resposta = menu(opcoes)
    if resposta == 1:
        readFile(database)
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        name = str(input("Nome: "))
        age = leiaInt("Idade: ")
        register(database, name, age)
    elif resposta == 3:
        print("Saindo do sistema...")
        break
    else:
        print("\033[31mERRO: Digite uma opção válida!\033[m")
    sleep(2)
