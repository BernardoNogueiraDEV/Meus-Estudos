largura = int(input('Qual largura da parede? '))
altura = int(input('Qual a altura da parede? '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a area de {}m², e sera necessario {}L de tinra para pintala.'.format(area, tinta))