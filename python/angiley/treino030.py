tupla = (['Fusca', 21], ['GOL', 15], ['Vectra', 10], ['Astra', 5], ['Mobi', 20])
mais_economico = tupla[0][0]

print(f'O carro mais econômico da lista é {mais_economico}')

for carro in tupla:
    nome = carro[0]
    consumo_por_km = carro[1]
    consumo_1000_km = 1000 / consumo_por_km
    custo = consumo_1000_km * 5.5
    print(f'\nO {nome} consome em uma viagem de 1000 quilômetros: {consumo_1000_km:.2f} L, que gastou R$ {custo:.2f}')
