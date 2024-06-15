p1 = input('Digite C de celcius para fahnreint ou digite F de fahnreint para celcius: ')
if p1 == 'C':
    c = float(input('Qual a temperatura em °C: '))
    f1 = ((9 * c) / 5) + 32
    print(f'{c}°C em fahnreint é {f1}°F')
elif p1 == 'F':
    f = float(input('Qual a temperatura em °F: '))
    c1 = (f - 32) * 5 / 9
    print(f'{f}°F em celcius é {c1}°C')