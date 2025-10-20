// Multiplicación de Matrices: Multiplica dos matrices válidas.

function multiplicarMatrices(matrizA, matrizB) {
    if (matrizA[0].length !== matrizB.length) {
        throw new Error("El número de columnas de A debe ser igual al número de filas de B.");
    }

    const resultado = [];
    const filasA = matrizA.length;
    const columnasA = matrizA[0].length;
    const columnasB = matrizB[0].length;

    for (let i = 0; i < filasA; i++) {
        resultado[i] = [];
        for (let j = 0; j < columnasB; j++) {
        resultado[i][j] = 0;
        }
    }

    for (let i = 0; i < filasA; i++) {
        for (let j = 0; j < columnasB; j++) {
        for (let k = 0; k < columnasA; k++) {
            resultado[i][j] += matrizA[i][k] * matrizB[k][j];
        }
        }
    }

    return resultado;
    }

    const A = [
    [1, 2, 3],
    [4, 5, 6]
    ];
    const B = [
    [7, 8],
    [9, 10],
    [11, 12]
    ];

const resultado = multiplicarMatrices(A, B);
console.log("Resultado de la multiplicación:");
console.table(resultado);
