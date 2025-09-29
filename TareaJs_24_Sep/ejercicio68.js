// Buscar y Reemplazar: Busca un valor en array y lo reemplaza por otro.

function buscarYReemplazar(array, valorBuscado, nuevoValor) {
    const index = array.indexOf(valorBuscado);
    if (index !== -1) {
        array[index] = nuevoValor;
    }
    return array;
}

console.log(buscarYReemplazar([1, 2, 3, 2], 2, 9)); 
