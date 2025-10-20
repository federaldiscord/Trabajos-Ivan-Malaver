// Filtrar Array: Filtra elementos según diferentes criterios.

function filtrarMayores(array, limite) {
    return array.filter(num => num > limite);
}

console.log(filtrarMayores([1, 5, 8, 2, 10], 5)); 
