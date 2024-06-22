from time import sleep
lista = []
while True:
    numeros = int(input('Digite um número inteiro: '))
    fim = str(input('Digite "Q" para finalizar e ver os resultados ou precione enter para continuar: ')).strip().upper()
    lista.append(numeros)
    media = (sum(lista)) / len(lista)
    maior = max(lista)
    menor = min(lista)
    if fim == 'Q':
        break
print('Gerando resultado...')
sleep(3)
print(f'A media entre eles é {media}')
print(f'O menor valor foi {menor}')
print(f'O maior valor foi {maior}')