// Máximo y Mínimo: Encuentra el valor máximo y mínimo en un array.

function encontrarMaxMin(array) {
    let max = array[0];
    let min = array[0];

    for (let i = 1; i < array.length; i++) {
        if (array[i] > max) max = array[i];
        if (array[i] < min) min = array[i];
    }

    return { max, min };
}

const datos = [7, 15, -2, 50, 8];
console.log(encontrarMaxMin(datos)); // { max: 50, min: -2 }
