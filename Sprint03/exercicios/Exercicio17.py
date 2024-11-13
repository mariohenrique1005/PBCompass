def divisao(lista):
    tamanho = len(lista) // 3
    lista1 = lista[:tamanho]
    lista2 = lista[tamanho:tamanho*2]
    lista3 = lista[tamanho*2:]
    return lista1, lista2, lista3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
p1, p2, p3 = divisao(lista)
print(p1, p2, p3)