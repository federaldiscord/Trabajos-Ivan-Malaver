// Frecuencia de Elementos: Cuenta cuántas veces aparece cada elemento en un array.

function frecuenciaElementos(array) {
    const frecuencia = {};

    for (let elemento of array) {
        if (frecuencia[elemento]) {
        frecuencia[elemento]++;
        } else {
        frecuencia[elemento] = 1;
        }
    }

    return frecuencia;
}

const datos = ["a", "b", "a", "c", "b", "a", "d"];
console.log(frecuenciaElementos(datos));
