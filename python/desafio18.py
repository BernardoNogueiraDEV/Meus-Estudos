import math
angulo = float(input('Digite um angulo: '))
radians = math.radians(angulo)
seno = math.sin(radians)
coss = math.cos(radians)
tan = math.tan(radians)
print(f'O angulo {angulo:.0f}° tem como seno {seno}, cosseno {coss}, e tangente {math.ceil(tan)}')