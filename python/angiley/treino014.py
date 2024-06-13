# Solicitar um número do usuário
numero = int(input("Digite um número: "))

# Verificar se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

# Exibir os primeiros 5 números ímpares
print("Os primeiros 5 números ímpares são:")
impares = []
countador = 0
num = 1

while countador < 5:
    if num % 2 != 0:
        impares.append(num)
        countador += 1
    num += 1

for impar in impares:
    print(impar)
