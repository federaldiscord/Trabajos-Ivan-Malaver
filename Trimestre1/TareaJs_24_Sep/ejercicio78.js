// Simetría de Matriz: Verifica si una matriz es simétrica.

function esSimetrica(matriz) {
    const n = matriz.length;

    for (let i = 0; i < n; i++) {
        if (matriz[i].length !== n) {
        return false;
        }
    }

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
        if (matriz[i][j] !== matriz[j][i]) {
            return false;
        }
        }
    }
    return true;
}

const matriz1 = [
  [1, 2, 3],
  [2, 5, 6],
  [3, 6, 9]
];

const matriz2 = [
  [1, 0, 3],
  [2, 5, 6],
  [3, 6, 9]
];

console.log("¿Matriz 1 es simétrica?", esSimetrica(matriz1));
console.log("¿Matriz 2 es simétrica?", esSimetrica(matriz2));
