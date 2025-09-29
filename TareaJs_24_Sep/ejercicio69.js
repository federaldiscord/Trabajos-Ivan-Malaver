// Combinar Arrays: Combina dos arrays ordenados en uno solo ordenado.

function combinarOrdenados(arr1, arr2) {
    let i = 0, j = 0;
    const resultado = [];

    while (i < arr1.length && j < arr2.length) {
        if (arr1[i] < arr2[j]) {
        resultado.push(arr1[i]);
        i++;
        } else {
        resultado.push(arr2[j]);
        j++;
        }
    }

    return resultado.concat(arr1.slice(i)).concat(arr2.slice(j));
}

console.log(combinarOrdenados([1, 3, 5], [2, 4, 6])); 
