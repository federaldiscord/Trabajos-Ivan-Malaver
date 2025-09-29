// Elementos Faltantes: Encuentra números faltantes en una secuencia.

function encontrarFaltantes(array) {
    const faltantes = [];
    const min = Math.min(...array);
    const max = Math.max(...array);

    for (let i = min; i <= max; i++) {
        if (!array.includes(i)) {
        faltantes.push(i);
        }
    }

    return faltantes;
}

console.log(encontrarFaltantes([1, 2, 4, 6, 7])); 
