numero = input("Digite um número inteiro: ")
try:
    numero_int= int(numero)
except ValueError:
    print("Você não digitou um valor inteiro, tente novamente")
    exit

posterior = numero_int + 1
print(f"O posterior é {posterior}")