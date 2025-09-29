// Calculadora de Propina: Calcula diferentes porcentajes de propina para una cuenta.

let cuenta = parseFloat(prompt("Ingrese el total de la cuenta:"));
let propina1 = cuenta * 0.1;
let propina2 = cuenta * 0.15;
let propina3 = cuenta * 0.2;
console.log(`Propina del 10%: ${propina1}`);
console.log(`Propina del 15%: ${propina2}`);
console.log(`Propina del 20%: ${propina3}`);