nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
nota3 = float(input('Digite a sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print(f'Sua media é de {media:.2f}, portando está aprovado!')
else:
    print(f'Sua media foi de {media:.2f}, portanto está reprovado!')