// Búsqueda en Array: Busca un elemento en un array.

function buscarIndice(array, elemento) {
    const indice = array.indexOf(elemento);
    return indice !== -1 ? indice : "Elemento no encontrado";
}

const frutas = ["manzana", "pera", "uva", "naranja"];
console.log(buscarIndice(frutas, "uva"));
console.log(buscarIndice(frutas, "banana"));
