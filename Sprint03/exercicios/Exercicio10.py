def remover_duplicados(listaB):
    return list(set(listaB))

lista=['abc', 'abc', 'abc', '123', 'abc', '123', '123']
lista_final = remover_duplicados(lista)
print(lista_final)