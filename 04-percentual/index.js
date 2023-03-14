const values = [['SP', 67836.43], ['RJ', 36678.66],
['MG', 29229.88], ['ES', 27165.48], ['Outros', 19849.53]]

const calculaPercentual = (values) => {
    const total = values.map((e) => e[1]).reduce((acc, cur) => acc + cur, 0);
    const estados = values.map((ele) => ele[0]);
    const percentual = values.map((e) => e[1]).map((ele) => ((ele / total) * 100).toFixed(2));
    const resposta = percentual.map((e, i) =>
        `${estados[i]} teve representação de ganhos de ${e}% sobre o total mensal da distribuidora.`);

    console.log(`O ganho mensal total da distribuidora foi de: R$ ${total}.`)
    return resposta.map((e) => console.log(e));
}

calculaPercentual(values);
