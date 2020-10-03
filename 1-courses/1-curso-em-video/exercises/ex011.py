# Condicoes Aninhadas
nome = str(input("Qual é seu nome? "))

if nome == "Marcos Vinicius":
    print("Wow, que nome bonito ;)")
elif nome == "Maria" or nome == "Bruna" or nome == "Lucas":
    print("Seu nome é bem popular no Brasil :)")
elif nome in "Jéssica Yasmin Maria Clara":
    print("Belo nome femino :D")
else:
    print("Seu nome não é tão bonito assim :(")

print("Tenha um bom dia, {}!".format(nome))
