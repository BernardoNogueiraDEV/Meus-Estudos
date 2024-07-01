numeros = []
while True:
    num = int(input("Digite um número (0 para parar): "))
    if num == 0:
        break
    numeros.append(num)
quantidade_numeros = len(numeros)
numeros_decrescente = sorted(numeros, reverse=True)
if 2 in numeros:
    esta_na_lista = "sim"
else:
    esta_na_lista = "não"
print(f"\nQuantidade de números digitados: {quantidade_numeros}")
print(f"Lista dos números em ordem decrescente: {numeros_decrescente}")
print(f"O número 2 foi digitado? {esta_na_lista}")
