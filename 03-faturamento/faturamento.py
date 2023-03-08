import json

with open("faturamento.json", encoding='utf-8') as f:
    data = json.load(f)

total = 0
arrayFaturamento = list()

for i in data:
    total = total + i['faturamento']
    arrayFaturamento.append(i['faturamento'])

for i in arrayFaturamento:
    if i == 0:
        arrayFaturamento.remove(i)

minFaturamento = min(arrayFaturamento)
maxFaturamento = max(arrayFaturamento)

print(minFaturamento)
print(maxFaturamento)
