// MCD y MCM: Calcula el máximo común divisor y mínimo común múltiplo.

let num1 = 12;
let num2 = 18;

let mcd = 1;
let mcm = num1 * num2;

for (let i = 1; i <= num1 && i <= num2; i++) {
    if (num1 % i === 0 && num2 % i === 0) {
        mcd = i;
    }
}

console.log(`El MCD de ${num1} y ${num2} es: ${mcd}`);
console.log(`El MCM de ${num1} y ${num2} es: ${mcm}`);