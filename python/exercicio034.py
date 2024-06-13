salario = float(input('Qual o salario? '))
if salario >= 1250:
    aumento = salario * (10 / 100) + salario
    print(f'Seu novo Salário com 10% de aumento é de R$ {aumento:.2f}')
else:
    aumento2 = salario * (15 / 100) + salario
    print(f'Seu novo salário com 15% de aumento é de R$ {aumento2:.2f}')