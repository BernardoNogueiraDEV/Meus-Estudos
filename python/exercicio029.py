# pergunta qual a velocidade do carro ao usuario
velocidade = float(input('Qual a velocidade do carro? '))
# Verifica se esta dentro do limite de velocidade, senao aplica a multa
if velocidade <= 80:
    print(f'Você está dentro do limite de velocidade')
else:
    multa = (velocidade - 80) * 7
    print(f'Você passou a {velocidade}Kmh, ultrapassando o limite e irá receber R${multa:.2f} de multa.')