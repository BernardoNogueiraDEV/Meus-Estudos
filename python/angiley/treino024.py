def fibonacci(n):
    fib_sequencia = [0, 1]
    
    
    for i in range(2, n):
        proximo_numero = fib_sequencia[-1] + fib_sequencia[-2]
        fib_sequencia.append(proximo_numero)
    
    return fib_sequencia


n = int(input("Digite um número inteiro para gerar a sequência de Fibonacci: "))


if n <= 0:
    print("Por favor, insira um número inteiro maior que zero.")
else:
    
    resultado = fibonacci(n)
    
    # Mostra a sequência de Fibonacci
    print(f"Os primeiros {n} elementos da sequência de Fibonacci são:")
    print(resultado)
