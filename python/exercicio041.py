print('*_'*10)
print('   Confederação Nacional de Natação')
print('*_'*10)

idade = int(input('Digite a idade do praticante: '))
if idade < 9 :
    print('O praticante vai para categoria MIRIM')
elif idade < 14:
    print('O praticante vai para categoria INFANTIL')
elif idade < 19:
    print('O praticante vai para categoria JUNIOR')
elif idade < 20:
    print('O praticante vai para categoria SÊNIOR')
else:
    print('O praticante vai para categoria MASTER')