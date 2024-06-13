cidade = input('Qual sua cidade? ')
s = cidade.split()
r = s[0].title()
c = 'Santo' in r
print(f'Sua cidade começa com Santo, portanto: {c}')