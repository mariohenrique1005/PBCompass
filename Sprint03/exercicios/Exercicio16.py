def separacao (v):
    separados=valores.split(",")
    soma=0
    for i in separados:
        soma=soma+int(i)
    return soma

valores="1,3,4,6,10,76"
vsomados=separacao(valores)
print(vsomados)