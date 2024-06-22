
while True:
    sexo = str(input('Digite o sexo da pessoa (M\F): ')).strip().lower()
    if sexo != str(sexo):
        continue
    elif sexo == 'm':
        print('É um homem')
        break
    elif sexo == 'f':
        print('É mulher')
        break