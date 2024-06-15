dia = float(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos km você andou com ele? '))
pago = (dia * 60) + (km * 0.15)
print(f'Total a pagar é R${pago}')