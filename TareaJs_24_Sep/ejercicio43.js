// Factorial con For: Calcula factorial usando bucle for.

let num = 5;
let factorial = 1;
for (let i = 1; i <= num; i++) {
    factorial *= i;
}
console.log(`El factorial de ${num} es: ${factorial}`);