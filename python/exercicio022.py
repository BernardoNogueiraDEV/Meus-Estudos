nome = input('Digite seu nome completo: ')
sem_espaço = nome.strip()
primeiro_nome = nome.split()
print(f'Seu nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Seu nome com todas as letras minúsculas: {nome.lower()}')
print(f'Seu nome sem considerar os espaços tem {len(sem_espaço)} letras')
print(f'Seu primeiro nome tem {len(primeiro_nome[0])} letras')