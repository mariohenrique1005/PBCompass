arquivo_txt = 'C:/Users/mario/Github/Sprint04/exercicios/number.txt'

with open (arquivo_txt, mode='r') as txt:
    num=list(map(int,txt))

num_pares=filter(lambda x:x%2==0,num)
maiores=sorted(num_pares, reverse=True)[:5]
soma=sum(maiores)
print(maiores)
print(soma)