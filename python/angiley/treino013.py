produto = float(input('Qual o valor da compra: '))
pago = float(input('Quanto você pagou: '))
troco = pago - produto
falta = produto - pago
if pago < produto:
    print(f'Falta R$ {falta:.2f}')
else:
    print(f'O valor do troco é R$ {troco:.2f}')