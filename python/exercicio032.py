ano = int(input('Em qual ano você está: '))
if ano % 4 == 0 or ano % 400 == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')