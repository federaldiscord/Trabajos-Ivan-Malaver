// Promedio de Array: Calcula el promedio de los elementos de un array.

function calcularPromedio(array) {
    let suma = 0;

    for (let i = 0; i < array.length; i++) {
    suma += array[i];
    }

    return suma / array.length;
}

const numeros = [10, 20, 30, 40, 50];
console.log("Promedio:", calcularPromedio(numeros)); // 30
