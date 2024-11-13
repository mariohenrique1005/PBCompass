def recebe (*args, **kwargs):
    for param in args:
        print (param)
    for param, valor in kwargs.items():
        print(valor)

recebe(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)