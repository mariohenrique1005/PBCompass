csv = 'D:/Users/mario/Documents/Compass/S3/Exercicios/actors.csv'
arquivo_saida = 'C:/Users/mario/Github/Sprint03/exercicios/ExercicioII/Etapa-5.txt'

receitas_atores = []

with open(csv, mode='r') as csv:
    cabecalho = csv.readline().strip().split(',')
    indice_ator = cabecalho.index("Actor")
    total_gross = cabecalho.index("Total Gross")

    for linha in csv:
        colunas = linha.strip().split(',')
        ator = colunas[indice_ator].strip()
        receita_bruta = float(colunas[total_gross].strip())
        receitas_atores.append((ator, receita_bruta))

receitas_ordenadas = sorted(receitas_atores, key=lambda x: -x[1])

with open(arquivo_saida, mode='w') as arquivo_saida:
    for ator, receita in receitas_ordenadas:
        arquivo_saida.write(f"{ator} - {receita:.2f}\n")
print("Resultado salvo com sucesso em 'etapa-5.txt'")