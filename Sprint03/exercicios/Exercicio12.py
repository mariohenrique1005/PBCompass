def my_map (list, f):
    nlista=[]
    for i in list:
        nlista.append(f(i))
    return nlista

def potencia (x):
    return x**2

entrada=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado=my_map(entrada,potencia)
print(resultado)