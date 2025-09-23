// Calculadora en JavaScript
function sumar(a, b) {
    return a + b;
}
function restar(a, b) {
    return a - b;
}
function multiplicar(a, b) {
    return a * b;
}
function dividir(a, b) {
    if (b != 0) {
        return a / b;
    } else {
        return "Error: División por cero no permitida.";
    }
}
console.log("Suma: " + sumar(5, 3));
console.log("Resta: " + restar(5, 3));
console.log("Multiplicación: " + multiplicar(5, 3));
console.log("División: " + dividir(5, 0));

input = prompt("Ingrese dos números separados por una coma (ejemplo: 5,3):");
var numeros = input.split(",");
var num1 = parseFloat(numeros[0]);
var num2 = parseFloat(numeros[1]);
typeof console.log("Suma: " + sumar(num1, num2));
typeof console.log("Resta: " + restar(num1, num2));
typeof console.log("Multiplicación: " + multiplicar(num1, num2));
typeof console.log("División: " + dividir(num1, num2));