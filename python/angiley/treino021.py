import sys
import os
import time
def maioridade(pessoas):
    lista_maiores = []
    lista_menores = []

    for i in range(7):
        ano = int(input(f'Digite o ano de nascimento da {i+1}ª pessoa: '))
        if ano < 2024:        
                
            idade = 2024 - ano
                
            if idade < 18:
                lista_menores.append(idade)
            else:
                lista_maiores.append(idade)
        else:
            print('Data de nascimento invalida!')
            print('Reiniciando...')
            time.sleep(3)
            os.execl(sys.executable, sys.executable, *sys.argv)
    
    quantidade_menor = len(lista_menores)
    quantidade_maior = len(lista_maiores)

    print(f'No total são {quantidade_maior} pessoas maiores de idade e {quantidade_menor} pessoas menores de idade')
maioridade(7)