// Descuento por Edad: Aplica descuentos según edad con ternario.

const descuentoPorEdad = edad =>
    edad < 0 ? "Edad inválida" :
    edad < 12 ? "50% de descuento" :
    edad < 18 ? "25% de descuento" :
    edad < 60 ? "10% de descuento" :
    "40% de descuento";

console.log(descuentoPorEdad(5));
console.log(descuentoPorEdad(15));
console.log(descuentoPorEdad(30));
console.log(descuentoPorEdad(70));
console.log(descuentoPorEdad(-1));
