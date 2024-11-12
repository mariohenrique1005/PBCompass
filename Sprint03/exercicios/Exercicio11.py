import json
with open('person.json', 'r') as file:
    dados = json.load(file)
print(dados)
