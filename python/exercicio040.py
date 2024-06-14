nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Sua média foi de {media}, portanto está reprovado.') 
elif media < 6.9:
    print(f'Sua média foi de {media}, portanto está de recuperação')
else:
    print(f'Sua média foi de {media}, portanto está aprovado. PARABÉNS!!')