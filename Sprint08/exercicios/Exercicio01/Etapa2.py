import csv

animais=['gato','cao','elefante','girafa','leao','onca','tigre','avestruz','galinha','pato',
         'boi','cavalo','passaro','formiga','besouro','abelha','tatu','capivara','ornitorrinco','tamandua']
animais.sort()
for i in animais:
    print(i)

with open('animais.csv', mode='w', newline='') as arquivo:
    writer=csv.writer(arquivo)
    for i in animais:
        writer.writerow([i])
print('Arquivo criado com sucesso')