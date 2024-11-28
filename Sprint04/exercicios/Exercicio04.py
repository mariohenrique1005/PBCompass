def calcular_valor_maximo(rec_operadores,rec_operandos) -> float:
    operacao = lambda op, par: (
        par[0] + par[1] if op == '+' else
        par[0] - par[1] if op == '-' else
        par[0] * par[1] if op == '*' else
        par[0] / par[1] if op == '/' else
        par[0] % par[1] if op == '%' else 
        None
    )
    resultados = map(lambda x: operacao(x[0], x[1]), zip(rec_operadores, rec_operandos))
    return max(resultados)

operadores = ['+','-','*','/','%']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
print(calcular_valor_maximo(operadores, operandos))