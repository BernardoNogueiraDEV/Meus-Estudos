import random
n1 = int(input('O computador pensou em um numero de 0 a 5, adivinhe: '))
sorteio = random.randint(0, 5)
if n1 == sorteio:
    print('Você venceu')
else:
    print('Você perdeu')