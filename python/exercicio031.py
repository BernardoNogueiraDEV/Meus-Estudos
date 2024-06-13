pergunta = float(input('Digite a distancia da sua viagem em KM? '))
if pergunta < 200:
    calculo_por_km_menor = pergunta * 0.5
    print(f'Sua viagem vai custar R$ {calculo_por_km_menor:.2f}')
else:
    calculo_por_km_maior = pergunta * 0.45
    print(f'Sua viagem vai custar R$ {calculo_por_km_maior:.2f}')