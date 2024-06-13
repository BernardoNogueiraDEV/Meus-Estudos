produto = float(input('Qual o preço do produto? '))
desconto = produto*5/100
final = produto - desconto
print('Seu produto com 5% de desconto acaba ficando {}.'.format(final))