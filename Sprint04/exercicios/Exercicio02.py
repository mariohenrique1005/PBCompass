def conta_vogais(texto:str)-> int:
    return len(list(filter(lambda char: char.lower() in 'aeiou', texto)))

entrada='Este e um teste de vogais'
print(conta_vogais(entrada))