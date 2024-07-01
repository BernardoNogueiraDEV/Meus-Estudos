# Lista para armazenar o número de vendedores em cada faixa salarial
salarios = [0] * 9

# Lista de vendas brutas dos vendedores
vendas_brutas = [3000, 4000, 500, 1500, 3200, 8500, 2500, 750, 10000]

# Calcula o salário e atualiza a lista de contadores
for vendas in vendas_brutas:
    salario = 200 + (0.09 * vendas)
    index = min(int(salario // 100) - 2, 8)
    salarios[index] += 1

# Exibe o resultado
faixas_salariais = [
    "R$200 - R$299",
    "R$300 - R$399",
    "R$400 - R$499",
    "R$500 - R$599",
    "R$600 - R$699",
    "R$700 - R$799",
    "R$800 - R$899",
    "R$900 - R$999",
    "R$1000 em diante"
]

for i in range(len(salarios)):
    print(f"{faixas_salariais[i]}: {salarios[i]} vendedor(es)")
