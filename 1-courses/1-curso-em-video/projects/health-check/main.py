import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://pudim.com.br")
except urllib.error.URLError:
    print("Site não acessível no momento :(")
except Exception as error:
    print(f"Algo errado -> {error.__cause__}")
else:
    print("Tudo certo com o site :)")
