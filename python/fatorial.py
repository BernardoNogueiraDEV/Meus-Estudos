def fatorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return ValueError('Não é possivel fazer com números negativos')
    elif not n.is_integer():
        return ValueError('somente números inteiros')
    else:
        return n * fatorial(n-1)
    

# Exemplo de uso da função
numero = float(input('Digite um número inteiro n negativo:'))
print(f"Fatorial de {numero}, {fatorial(numero)}")