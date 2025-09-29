// Clasificador de Triángulos: Clasifica triángulos por sus lados (equilátero, isósceles, escaleno).

let lado1 = parseFloat(prompt("Ingrese el primer lado del triángulo:"));
let lado2 = parseFloat(prompt("Ingrese el segundo lado del triángulo:"));
let lado3 = parseFloat(prompt("Ingrese el tercer lado del triángulo:"));

if (lado1 === lado2 && lado2 === lado3) {
    console.log("El triángulo es equilátero.");
} else if (lado1 === lado2 || lado2 === lado3 || lado1 === lado3) {
    console.log("El triángulo es isóceles.");
} else {
    console.log("El triángulo es escaleno.");
}