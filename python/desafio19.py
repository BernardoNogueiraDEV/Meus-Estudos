import random
alunos = []
for i in range(4):
    nome = input(f'Digite o nome do aluno {i+1}: ')
    alunos.append(nome)
escolhido = random.choice(alunos)
print(f'O aluno escolhido para apagar o quadro é {escolhido}')
