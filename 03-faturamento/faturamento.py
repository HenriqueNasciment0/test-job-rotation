import json

with open("faturamento.json", encoding='utf-8') as f:
    data = json.load(f)

total = 0
arrayFaturamento = list()

for i in data:
    total = total + i['faturamento']
    arrayFaturamento.append(i['faturamento'])

print(arrayFaturamento)
