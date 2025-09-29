// Suma de Matrices: Suma dos matrices de igual dimensión.

function sumarMatrices(matrizA, matrizB) {
    if (matrizA.length !== matrizB.length || matrizA[0].length !== matrizB[0].length) {
        throw new Error("Las matrices deben tener las mismas dimensiones.");
    }

    const matrizResultado = [];

    for (let i = 0; i < matrizA.length; i++) {
        matrizResultado[i] = [];
        for (let j = 0; j < matrizA[i].length; j++) {
        matrizResultado[i][j] = matrizA[i][j] + matrizB[i][j];
        }
    }

    return matrizResultado;
    }

    const A = [
    [1, 2, 3],
    [4, 5, 6]
    ];

    const B = [
    [7, 8, 9],
    [1, 2, 3]
    ];

const resultado = sumarMatrices(A, B);
console.log("Resultado de la suma de matrices:");
console.table(resultado);
