// Tipo de Triángulo: Clasificación compacta de triángulos.

const tipoTriangulo = (a, b, c) =>
    a + b <= c || a + c <= b || b + c <= a
        ? "No es un triángulo"
        : a === b && b === c
        ? "Equilátero"
        : a === b || a === c || b === c
        ? "Isósceles"
        : "Escaleno";

console.log(tipoTriangulo(3, 3, 3));
console.log(tipoTriangulo(3, 3, 4));
console.log(tipoTriangulo(3, 4, 5));
console.log(tipoTriangulo(1, 2, 3));
