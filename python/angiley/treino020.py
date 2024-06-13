# Solicitar o nome completo do usuário
nome_completo = input("Digite seu nome completo: ")

# Inicializar contadores de vogais e consoantes
vogais = 0
consoantes = 0

# Definir conjuntos de vogais
conjunto_vogais = "aeiouAEIOU"

# Contar vogais e consoantes
for letra in nome_completo:
    if letra.isalpha():  # Verificar se o caractere é uma letra
        if letra in conjunto_vogais:
            vogais += 1
        else:
            consoantes += 1

# Calcular o total de letras
total_letras = vogais + consoantes

# Exibir os resultados
print(f"Seu nome completo tem {vogais} vogais e {consoantes} consoantes.")
print(f"O total de letras no seu nome é: {total_letras}")
