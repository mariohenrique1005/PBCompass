from functools import reduce

def calcula_saldo(rec_lancamentos) -> float:
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], rec_lancamentos)
    saldo = reduce(lambda acc, x: acc + x, valores)
    return saldo

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]
print(calcula_saldo(lancamentos))