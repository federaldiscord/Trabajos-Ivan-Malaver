// Suma de Dígitos: Calcula la suma de los dígitos de un número.

let num = 3006898362;
let suma = 0;
while (num > 0) {
    let digito = num % 10;
    suma += digito;
    num = Math.floor(num / 10);
}
console.log(`La suma de los dígitos de ${num} es: ${suma}`);