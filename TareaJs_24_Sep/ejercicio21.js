// Calculadora con Switch: Implementa una calculadora usando switch para las operaciones.

let num1 = parseFloat(prompt("Ingrese el primer número:"));
let num2 = parseFloat(prompt("Ingrese el segundo número:"));
let operacion = prompt("Ingrese la operación (+, -, *, /):");

let resultado;

switch (operacion) {
    case "+":
        resultado = num1 + num2;
        break;
    case "-":
        resultado = num1 - num2;
        break;
    case "*":
        resultado = num1 * num2;
        break;
    case "/":
        resultado = num1 / num2;
        break;
    default:
        console.log("Operación inválida.");
        break;
}

if (resultado !== undefined) {
    console.log(`El resultado es: ${resultado}`);
}