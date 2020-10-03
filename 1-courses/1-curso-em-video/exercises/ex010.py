# Cores no Terminal

# Style
# 0 none, 1 bold, 4 underline, 7 negativo

# Text 3x - Background 4x
# 0 branco, 1 vermelho, 2 verde, 3 amarelo, 4 azul, 5 magenta, 6 ciano, 7 cinza

# Escrita direta
print("\033[0;37;43mOlá Mundo!\033[m")
print("\033[1;30;41mOlá Mundo!\033[m")
print("\033[4;34;43mOlá Mundo!\033[m")
print("\033[7;30:46mOlá Mundo!\033[m")
print("\033[0;30;41mOlá Mundo!\033[m")
print("\033[31mOlá Mundo!\033[m")
print("\033[32mOlá Mundo!\033[m")

# Escrita com variaveis
cores = {
    "limpa": "\033[m",
    "azul": "\033[34m",
    "amarelo": "\033[33m",
    "pretoebranco": "\033[7:30m",
}
print("Muito prazer em {}te conhecer{}".format(cores["amarelo"], cores["limpa"]))
