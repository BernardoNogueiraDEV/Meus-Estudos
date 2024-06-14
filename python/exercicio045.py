import random
import os
import sys

def jogar():
    lista = ['pedra', 'papel', 'tesoura']

    nome_usuario = input('Digite seu nome: ')

    while True:
        pergunta = input('''Escolha: 
            Pedra
            Papel
            Tesoura
            ''').lower()

        if pergunta not in lista:
            print('Você digitou algo errado, tente novamente')
            continue

        escolha_maquina = random.choice(lista)

        if pergunta == 'pedra' and escolha_maquina == 'tesoura':
            print(f'Parabéns {nome_usuario}, você ganhou!!!')

        elif pergunta == 'pedra' and escolha_maquina == 'pedra':
            print(f'A máquina também escolheu pedra. EMPATE!!!')

        elif pergunta == 'pedra' and escolha_maquina == 'papel':
            print(f'A máquina escolheu papel. Você perdeu.')

        elif pergunta == 'papel' and escolha_maquina == 'tesoura':
            print(f'A máquina escolheu tesoura. Você perdeu.')

        elif pergunta == 'papel' and escolha_maquina == 'papel':
            print(f'A máquina também escolheu papel. EMPATE!!!')

        elif pergunta == 'papel' and escolha_maquina == 'pedra':
            print(f'Parabéns {nome_usuario}, você ganhou!!!')

        elif pergunta == 'tesoura' and escolha_maquina == 'tesoura':
            print(f'A máquina também escolheu tesoura. EMPATE!!!')

        elif pergunta == 'tesoura' and escolha_maquina == 'pedra':
            print(f'A máquina escolheu pedra. Você perdeu.')

        elif pergunta == 'tesoura' and escolha_maquina == 'papel':
            print(f'Parabéns {nome_usuario}, você ganhou!!!')
        
        fim = input('Digite "r" para reiniciar ou "q" para acabar o jogo: ').lower()

        if fim == 'r':
            print("Reiniciando o jogo...")
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            print("Saindo do jogo...")
            break

if __name__ == "__main__":
    jogar()