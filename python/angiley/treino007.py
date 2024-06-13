# Calculadora de IMC
peso = float(input('Qual o seu peso: '))
altura = float(input('Qual seu altura: '))
# Calcular o IMC
imc = peso / (altura * altura)
if imc <= 18.5:
    print(f'Seu imc é de {imc}Kg/m², portanto está abaixo do peso')
elif imc <= 24.9:
    print(f'Seu imc é de {imc}Kg/m², portanto está com o peso adequado')
elif imc <= 29.9:
    print(f'Seu imc é de {imc}Kg/m², portanto está com sobrepeso')
elif imc <= 34.9:
    print(f'Seu imc é de {imc}Kg/m², portanto está com obesidade grau 1')
elif imc <= 39.9:
    print(f'Seu imc é de {imc}Kg/m², portanto está com obesidade grau 2 ')
else:
    print('Seu imc é de {imc}Kg/m², portanto você está com obesidade mórbida')