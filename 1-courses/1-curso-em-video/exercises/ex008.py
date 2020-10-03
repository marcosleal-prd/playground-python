frase = "Curso em Vídeo de Python"
# frase = '   Aprenda Python  '

# Fatiamento
print(frase[9:15])
print(frase[9:15:2])
print(frase[:15])
print(frase[16:])
print(frase[0::2])

# Analise
print("LEN: ", len(frase))
print("COUNT: ", frase.count("o"))
print("COUNT FATIADO: ", frase.count("o", 0, 13))
print("FIND: ", frase.find("deo"))
print("FIND: ", frase.find("Android"))
print("IN: ", "Curso" in frase)

# Transformacao
print("REPLACE: ", frase.replace("Python", "Android"))
print("UPPER: ", frase.upper())
print("LOWER: ", frase.lower())
print("CAPITALIZE: ", frase.capitalize())
print("TITLE: ", frase.title())
print("STRIP: ", frase.strip())
print("RSTRIP: ", frase.rstrip())
print("LSTRIP: ", frase.lstrip())
print("SPLIT: ", frase.split())
print("JOIN: ", "_".join(frase.split()))
