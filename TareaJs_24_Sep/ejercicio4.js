// Calculadora de Edad: Pide el año de nacimiento y calcula la edad actual.

let ano_nacimiento = parseInt(prompt("Ingrese su año de nacimiento:"));
let ano_actual = new Date().getFullYear();
let edad = ano_actual - ano_nacimiento;
console.log(`Tu edad es: ${edad}`);