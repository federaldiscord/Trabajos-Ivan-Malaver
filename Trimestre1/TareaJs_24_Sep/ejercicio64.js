// Unión e Intersección: Encuentra unión e intersección de dos arrays.

function unionArrays(array1, array2) {
    return [...new Set([...array1, ...array2])];
}

function interseccionArrays(array1, array2) {
    return array1.filter(elemento => array2.includes(elemento));
}

const A = [1, 2, 3, 4, 5];
const B = [4, 5, 6, 7, 8];

console.log("Unión:", unionArrays(A, B));
console.log("Intersección:", interseccionArrays(A, B));
