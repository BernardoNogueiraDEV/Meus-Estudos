preco = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o valor do desconto: '))
porcentagem = desconto / 100
print(f'O seu produto com {desconto:.0f}% de desconto custa R$ {preco - (preco * porcentagem):.2f}')