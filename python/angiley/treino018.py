# Função para gerar um número pseudo-aleatório entre 1 e 10
def numero_pseudo_aleatorio(seed):
    # Gerador linear congruente simples
    # Fórmula: Xn+1 = (a * Xn + c) % m
    a = 1103515245
    c = 12345
    m = 2**32
    seed = (a * seed + c) % m
    return 1 + (seed % 10)

# Inicializar a semente (seed) com um valor arbitrário
seed = 54321  # Pode ser qualquer valor inteiro

# Gerar o número secreto
numero_secreto = numero_pseudo_aleatorio(seed)

# Variável booleana para controlar o loop
adivinhou = False

print("Tente adivinhar o número secreto entre 1 e 10.")

while not adivinhou:
    # Solicitar uma tentativa ao usuário
    tentativa = int(input("Digite sua tentativa: "))
    
    # Verificar a tentativa do usuário
    if tentativa == numero_secreto:
        print("Parabéns! Você adivinhou o número secreto.")
        adivinhou = True
    elif tentativa < numero_secreto:
        print("O número secreto é maior. Tente novamente.")
    else:
        print("O número secreto é menor. Tente novamente.")
