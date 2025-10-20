// Camino en Matriz: Encuentra caminos posibles en una matriz.

function encontrarCaminos(matriz) {
  const caminos = [];
  const filas = matriz.length;
  const columnas = matriz[0].length;

  function backtrack(i, j, camino) {
    if (i >= filas || j >= columnas) return;

    camino.push(matriz[i][j]);

    if (i === filas - 1 && j === columnas - 1) {
      caminos.push([...camino]);
    } else {
      backtrack(i, j + 1, camino);

      backtrack(i + 1, j, camino);
    }

    camino.pop();
  }

  backtrack(0, 0, []);
  return caminos;
}

const matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

console.log("Caminos posibles:");
console.log(encontrarCaminos(matriz));
