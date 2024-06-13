salario_inicial = float(input('Qual o salario do funcionario(a)? '))
porcentagem_de_aumento = float(input('Em quanto você deseja aumentar o salario dele(a) em porcentagem? '))
novo = salario_inicial + (salario_inicial * porcentagem_de_aumento/100)
print('O novo salario da pessoa é {} reais.'.format(novo))