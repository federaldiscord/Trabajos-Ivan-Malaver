// Rotar Matriz 90°: Rota una matriz 90 grados en sentido horario.

function rotarMatriz90(matriz) {
    const n = matriz.length;
    const resultado = Array.from({ length: n }, () => Array(n).fill(0));

    for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        resultado[j][n - 1 - i] = matriz[i][j];
    }
    }

    return resultado;
}

const matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

console.log("Matriz original:");
console.table(matriz);

console.log("Matriz rotada 90°:");
console.table(rotarMatriz90(matriz));
