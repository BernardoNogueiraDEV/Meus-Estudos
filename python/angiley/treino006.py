n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um: '))
n3 = int(input('Digite outro: '))
if n1 >= n2 >= n3:
    print(f'{n1} é o maior')
elif n1 >= n3 >= n2:
    print(f'{n1} é o maior')
elif n2 >= n1 >= n3:
    print(f'{n2} é o maior')
elif n2 >= n3 >= n1:
    print(f'{n2} é o maior')
elif n3 >= n1 >= n2:
    print(f'{n3} é o maior')
elif n3 >= n2 >= n1:
    print(f'{n3} é o maior')