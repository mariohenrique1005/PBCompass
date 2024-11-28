def maiores_que_media(rec_conteudo:dict)->list:
    media=sum(rec_conteudo.values())/len(rec_conteudo)
    acima=[(nome,preco) for nome, preco in rec_conteudo.items() if preco>media]
    produtos_ordenados=sorted(acima, key=lambda x: x[1])
    return produtos_ordenados

conteudo={
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
    }
lista=maiores_que_media(conteudo)
print(lista)