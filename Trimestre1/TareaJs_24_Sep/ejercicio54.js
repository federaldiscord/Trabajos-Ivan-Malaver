// Ordenamiento Burbuja: Ordena un array usando el método burbuja.

function ordenamientoBurbuja(array) {
    let n = array.length;
    let intercambiado;

    do {
        intercambiado = false;
        for (let i = 0; i < n - 1; i++) {
        if (array[i] > array[i + 1]) {
            let temp = array[i];
            array[i] = array[i + 1];
            array[i + 1] = temp;
            intercambiado = true;
        }
        }
        n--;
    } while (intercambiado);

    return array;
}

const numeros = [5, 3, 8, 4, 2];
console.log("Array original:", numeros);
console.log("Array ordenado:", ordenamientoBurbuja(numeros));
