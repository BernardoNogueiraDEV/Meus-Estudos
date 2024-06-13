import math
co = float(input('Qual o comprimento do ceteto oposto do triângulo retângulo? '))
ca = float(input('Qual o comprimento do cateto adjacente do triângulo retângulo? '))
hi = math.sqrt(co ** 2 + ca ** 2)
print(f'O comprimento da hipotenusa é {hi:.2f}')