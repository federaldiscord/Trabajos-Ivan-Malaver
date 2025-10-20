// Número Primo: Verifica si un número es primo.

let num = 13;
let esPrimo = true;

for (let i = 2; i < num; i++) {
    if (num % i === 0) {
        esPrimo = false;
        break;
    }
}

if (esPrimo) {
    console.log(num + " es primo.");
} else {
    console.log(num + " no es primo.");
}