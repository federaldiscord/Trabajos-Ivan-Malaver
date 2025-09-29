// calculadora de IMC: Calcula el Índice de Masa Corporal (peso / altura2).

let peso = parseFloat(prompt("Ingrese su peso en kg:"));
let altura = parseFloat(prompt("Ingrese su altura en metros:"));
let imc = peso / (altura * altura);
console.log(`Su IMC es: ${imc}`);