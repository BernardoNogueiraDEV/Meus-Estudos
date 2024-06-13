print('-*'*20)
print('          Emprestimo Bancário')
print('-*'*20)

valor_casa = float(input('Digite o valor da casa: '))
salario_usuario = float(input('Digite o salário do comprador: '))
quantos_anos = int(input('Em quantos anos o comprador deseja pagar: '))
prestacao = valor_casa / quantos_anos / 12
exceder_salario = salario_usuario * 0.30

if prestacao < exceder_salario:
    print(f'A casa custa R$ {valor_casa:.2f}. O comprador decidiu pagar em {quantos_anos} anos com suaves prestações de R$ {prestacao:.2f}')
elif prestacao > exceder_salario:
    print(f'A casa do valor de R$ {valor_casa:.2f}. Foi negado o emprestimo bancário pois o valor da parcela excede 30% do seu salário')