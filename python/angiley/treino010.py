lado1 = float(input('Digite um valor para um dos lados de um triângulo: '))
lado2 = float(input('Digite um valor para um outro lado de um triângulo: '))
lado3 = float(input('Digite um valor para um outro lado de um triângulo: '))
if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado1 <= lado3 or lado2 + lado3 <= lado1 or lado3 + lado1 <= lado2 or lado3 + lado2 <= lado1:
    if lado1 == lado2 == lado3 or lado1 == lado3 == lado2 or lado2 == lado1 == lado3 or lado2 == lado3 == lado1 or lado3 == lado1 == lado2 or lado3 == lado2 == lado1:
        print('É um triângulo equilátero pois todos os lado possuem a mesma medida')
    elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado1 != lado3 or lado2 == lado3 != lado1 or lado3 == lado1 != lado2 or lado3 == lado2 != lado1:
        print('É um triângulo isósceles pois dois lados possuem a mesma medida')
    elif lado1 != lado2 != lado3 or lado1 != lado3 != lado2 or lado2 != lado1 != lado3 or lado2 != lado3 != lado1 or lado3 != lado1 != lado2 or lado3 != lado2 != lado1:
        print('É um triângulo escaleno pois todos os lados possuem medidas diferentes')
    else:
        print('É um triângulo acutângulo pois todos os ângulos são agudos')
else:
    print('Não é possivel com esses valores pois a soma de dois lados tem que ser menor ou igual que a do terceiro lado para se formar um triângulo')