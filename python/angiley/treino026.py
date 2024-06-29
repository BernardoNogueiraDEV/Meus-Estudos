tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
'onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove',
'vinte','vinte e um','vinte e dois','vinte e três','vinte e quatro','vinte e cinco',
'vinte e seis','vinte e sete','vinte e oito','vinte e nove','trinta','trinta e um',
'trinta e dois','trinta e três','trinta e quatro','trinta e cinco','trinta e seis',
'trinta e sete','trinta e oito','trinta e nove','quarenta')

while True:
    try:
        print(f'Digite um número entre 0 e 40:')
        numero = int(input(''))
        print(tupla[numero])
        break
    except ValueError:
        print('Erro Você digitou algo errado')
