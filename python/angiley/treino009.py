idade = int(input('Digite sua idade: '))
if idade <= 2 :
    print(f'Você é um bebê')
elif idade <= 12:
    print(f'Você é uma criança')
elif idade <= 17:
    print(f'Você é um adolecente')
elif idade <= 64 :
    print(f'Você é um adulto')
else:
    print(f'Você é um idoso')