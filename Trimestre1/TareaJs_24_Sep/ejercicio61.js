// Suma de Elementos: Calcula la suma de todos los elementos de un array.

function sumarElementos(array) {
    let suma = 0;
    for (let i = 0; i < array.length; i++) {
        suma += array[i];
    }
    return suma;
}

console.log(sumarElementos([1, 2, 3, 4, 5]));
