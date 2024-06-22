# Inicialização das variáveis
total_idade = 0
soma_idades_mulheres = 0
homem_mais_velho_nome = ""
homem_mais_velho_idade = -1
quantidade_mulheres_menos_20 = 0

# Loop para leitura dos dados
for i in range(8):
    print(f"Pessoa {i + 1}:")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").strip().upper()

    # Acumulando a idade total para calcular a média
    total_idade += idade

    if sexo == 'F':
        # Somando as idades das mulheres
        soma_idades_mulheres += idade
        # Contando quantas mulheres têm menos de 20 anos
        if idade < 20:
            quantidade_mulheres_menos_20 += 1
    elif sexo == 'M':
        # Verificando se é o homem mais velho
        if idade > homem_mais_velho_idade:
            homem_mais_velho_idade = idade
            homem_mais_velho_nome = nome

# Calculando a média de idade do grupo
media_idade = total_idade / 8

# Mostrando os resultados
print("\nResultados:")
print(f"Média de idade do grupo: {media_idade:.2f} anos")
print(f"Soma das idades das mulheres: {soma_idades_mulheres} anos")
print(f"Nome do homem mais velho: {homem_mais_velho_nome}")
print(f"Quantidade de mulheres com menos de 20 anos: {quantidade_mulheres_menos_20}")
