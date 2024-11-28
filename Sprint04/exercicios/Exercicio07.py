def pares_ate(rec_n: int):
    for i in range(2, rec_n+1, 2):
        yield i

n=20
for i in pares_ate(n):
    print(i)