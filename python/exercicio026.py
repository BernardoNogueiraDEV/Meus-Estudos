frase = str(input('Digite uma frase: ')).lower().strip()
print(f'A letra A aparece {frase.count('a')} vezes.')
print(f'A aparece na primeira vez na posição {frase.find('a')+ 1}. ')
print(f'A pararece no final na posição {frase.rfind('a')}.')