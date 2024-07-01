lista = []

for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor numérico: "))
    
    
    inserido = False
    for j in range(len(lista)):
        if valor < lista[j]:
            lista.insert(j, valor)
            inserido = True
            break
    
    
    if not inserido:
        lista.append(valor)

print("\nLista ordenada:", lista)
