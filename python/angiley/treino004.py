salario = float(input('Digite o valor do salário do seu funcionario(a): '))
aumento = float(input('Qual a porcentagem que você deseja aumentar o salário: '))
porcentagem = aumento / 100
print(f'O salário com o aumento de {aumento:.0f}% fica R$ {salario * porcentagem + salario:.2f}')