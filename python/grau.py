def celcius_para_fahreint(celcius):
    return (celcius * 9/5) + 32
def fahreint_para_celcius(fahreint):
    return (fahreint - 32) * 5/9
opcao = input('Digite C para transformar celcius para fahreint, ou digite F para fahreint para celcius:' )
if opcao == 'C':
    celcius = float(input('Digite o valor em celcius:'))
    print('O valor em fahreint é:', celcius_para_fahreint(celcius))
elif opcao == 'F':
    fahreint = float(input('Digite o valor em fahreint:'))
    print('O valor em celcius é:', fahreint_para_celcius(fahreint))
else:
    print('Coloque um valor valido!')