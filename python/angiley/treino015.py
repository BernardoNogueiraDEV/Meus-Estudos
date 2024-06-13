# Cria uma lista para armazenar os dados
lista = []
# Laço de repetição para pedir os dados
for i in range(3):
    numeros = int(input(f'Digite o {i+1}º número: '))
    # Adiciona o número ao final da lista
    lista.append(numeros)
# Retira o menor número da lista
minimo = min(lista)
# Imprimi qual é o menor
print(f'O menor número entre eles é o {minimo}')
# Da o número inicial para o laço de repetição while
inicio = 0
print(f'Os numeros de 1 ate {minimo} são:')
while inicio < minimo:
    # Teste lógico
    if inicio % 2 != 0:
        inicio += 1
        print(f'{inicio} é par')
    else:
        inicio += 1
        print(f'{inicio} é impar')