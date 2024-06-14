idade  = float(input('Digite sua idade: '))
if idade < 18:
    falta = 18 - idade
    if falta > 1:
        print(f'Você ainde tem que se alistar no serviço militar. Falta {falta} anos')
    else:
        print(f'Você ainde tem que se alistar no serviço militar. Falta {falta} ano')
elif idade == 18:
    print(f'Está na hora já de você se alistar no serviço militar')
else:
    falta = idade - 18
    if falta < 1:
        print(f'Já passou da hora de você se alistar. Você está {falta} anos atrasado.')
    else:
        print(f'Já passou da hora de você se alistar. Você está {falta} ano atrasado.')