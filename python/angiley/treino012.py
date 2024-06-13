pessoa1 = [str(input('Qual o nome da primeira pessoa: ')), int(input('Qual a idade dele(a): '))]
pessoa2 = [str(input('Qual o nome da segunda pessoa: ')), int(input('Qual a idade dele(a): '))]
if pessoa1[1] > pessoa2[1]:
    print(f'{pessoa1[0]} é mais velho que {pessoa2[0]}')
else:
    print(f'{pessoa2[0]} é mais velho que {pessoa1[0]}')