import json

with open("faturamento.json", encoding='utf-8') as f:
    data = json.load(f)

total = 0
arrayFaturamento = list()
baseMedia = 0
qntDias = 0

for i in data:
    total = total + i['faturamento']
    arrayFaturamento.append(i['faturamento'])

for i in arrayFaturamento:
    if i == 0:
        arrayFaturamento.remove(i)
    baseMedia = baseMedia + i

mediaMensal = round(baseMedia / len(arrayFaturamento))

for i in arrayFaturamento:

    if i > mediaMensal:
        qntDias = qntDias + 1

minFaturamento = min(arrayFaturamento)
maxFaturamento = max(arrayFaturamento)


print(f'O menor faturamento no mês foi de: ${minFaturamento}.\n')
print(f'O maior faturamento no mês foi de: ${maxFaturamento}.\n')
print(f'Tivemos nesse mês, {qntDias} dias com faturamento acima da média mensal!\n')
