# Tratamento de Erros e Execeçoes
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    print("Algo errado com os tipos informados :(")
except ZeroDivisionError:
    print("Não é possível dividir por ZERO :(")
except KeyboardInterrupt:
    print("Usuário preferiu desistir :(")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
    print(f"Deu certo, o resultado é: {r}")
finally:
    print("\nVolte sempre ;)")
