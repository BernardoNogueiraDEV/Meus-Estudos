def decimal_para_binario(numero_decimal):
    if numero_decimal == 0:
        return "0"
    
    binario = ""
    while numero_decimal > 0:
        resto = numero_decimal % 2
        binario = str(resto) + binario
        numero_decimal = numero_decimal // 2
    
    return binario

def decimal_para_octal(numero_decimal):
    if numero_decimal == 0:
        return "0"
    
    octal = ""
    while numero_decimal > 0:
        resto = numero_decimal % 8
        octal = str(resto) + octal
        numero_decimal = numero_decimal // 8
    
    return octal

def decimal_para_hexadecimal(numero_decimal):
    if numero_decimal == 0:
        return "0"
    
    hexadecimal = ""
    while numero_decimal > 0:
        resto = numero_decimal % 16
        if resto < 10:
            hexadecimal = str(resto) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + resto - 10) + hexadecimal
        numero_decimal = numero_decimal // 16
    
    return hexadecimal

# Leitura do número inteiro do usuário
numero_decimal = int(input("Digite um número inteiro: "))

# Escolha da base de conversão
print("Escolha a base de conversão:")
print("1 para binário")
print("2 para octal")
print("3 para hexadecimal")
escolha = int(input("Digite sua escolha (1, 2 ou 3): "))

# Conversão e impressão do resultado
if escolha == 1:
    resultado = decimal_para_binario(numero_decimal)
    print(f"O número decimal {numero_decimal} em binário é {resultado}")
elif escolha == 2:
    resultado = decimal_para_octal(numero_decimal)
    print(f"O número decimal {numero_decimal} em octal é {resultado}")
elif escolha == 3:
    resultado = decimal_para_hexadecimal(numero_decimal)
    print(f"O número decimal {numero_decimal} em hexadecimal é {resultado}")
else:
    print("Escolha inválida. Por favor, escolha 1, 2 ou 3.")
