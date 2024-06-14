# Condições aninhadas
preco_produto = float(input('Digite o preço do produto: '))
cartao_ou_dinheiro = str(input('É no cartao ou no dinheiro: (cartao\dinheiro): ')).lower()

if cartao_ou_dinheiro == 'cartao':
    vista_ou_parcelado = str(input('À vista ou parcelado: (vista\parcelado): ')).lower()
    if vista_ou_parcelado == 'vista':
        desconto_cartao = preco_produto * (5 / 100)
        print(f'O preço do produto à vista no cartão fica R$ {preco_produto - desconto_cartao:.2f}')
    elif vista_ou_parcelado == 'parcelado':
        metodo_do_parcelamento = str(input('Digite de quantas vezes você deseja parcelar: (2x\3x)'))
        if metodo_do_parcelamento == '2x':
            print(f'Dividido em 2x o produto fica R$ {preco_produto / 2:.2f} mensais.')
        elif metodo_do_parcelamento == '3x':
            juros = 20 /100
            print(f'Dividido em 3x o produto fica R$ {preco_produto * juros + preco_produto:.2f} mensais.')
        else:
            print('Digite algo válido')
    else:
            print('Digite algo válido')
else:
    a_vista = str(input('Digite o metodo de pagamento: (dinheiro\cheque): ')).lower()
    if a_vista == 'dinheiro':
        a_vista_desconto_dinheiro = preco_produto * (10 / 100)
        print(f'O preço do produto à vista no dinheiro fica {preco_produto - a_vista_desconto_dinheiro:.2f}')
    else:
        a_vista_desconto_dinheiro = preco_produto * (10 / 100)
        print(f'O preço do produto à vista no cheque fica {preco_produto - a_vista_desconto_dinheiro}')