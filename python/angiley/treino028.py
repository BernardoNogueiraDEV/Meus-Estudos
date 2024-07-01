tupla =(
    'Flamengo',
    'Botafogo',
    'Bahia',
    'Palmeiras',
    'Cruzeiro',
    'Athletico-PR',
    'Bragantino',
    'São Paulo',
    'Internacional',
    'Atlético-MG',
    'Fortaleza',
    'Juventude',
    'Cuiabá',
    'Criciúma',
    'EC Vitória',
    'Vasco da Gama',
    'Atlético-GO',
    'Corinthians',
    'Grêmio',
    'Fluminense')
print(f'Os 5 ultimos colocados do brasileirão 2024 são:')
print(tupla[-1:-6:-1])

print('\nOs ultimos 4 colocados:')
print(tupla[-1:-5:-1])

print('\nO placar em ordem alfabetica:')
print(sorted(tupla))

print('\nO São Paulo esta na posição:')
posição = tupla.index('São Paulo')+ 1
print(f'{posição}°, lugar do campeonato brasileiro 2024.')    