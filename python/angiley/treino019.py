while True:
    entrada = input("Digite 'X' para parar o processamento: ")
    
    if entrada.upper() == 'X':
        print("O usuário parou o processamento.")
        break
    
    print("Você digitou:", entrada)
