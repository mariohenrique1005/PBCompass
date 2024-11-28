import csv

with open("estudantes.csv","r", encoding="utf-8") as csv_estudantes:
    estudantes=csv.reader(csv_estudantes)
    relatorio=[]
    for linha in estudantes:
        nome=linha[0]
        notas=list(map(int, linha[1:]))
        maiores=sorted(notas,reverse=True)[:3]
        media=round(sum(maiores)/3, 2)
        relatorio.append((nome, maiores, media))
        
    relatorio=sorted(relatorio, key=lambda x: x[0])
    for nome, maiores, media in relatorio:
        print(f"Nome: {nome} Notas: {maiores} Média: {media}")