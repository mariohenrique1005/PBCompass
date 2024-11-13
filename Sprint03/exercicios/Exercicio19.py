import random
random_list=random.sample(range(500), 50)
random_list.sort()
n_elementos=len(random_list)
mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0
if n_elementos % 2 == 1:
    mediana=random_list[n_elementos//2]
else:
    meio1=random_list[n_elementos//2-1]
    meio2=random_list[n_elementos//2]
    mediana=(meio1+meio2)/2
media=sum(random_list)/len(random_list)
valor_minimo=min(random_list)
valor_maximo=max(random_list)
print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")