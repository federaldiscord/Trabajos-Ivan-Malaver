// Secuencia Fibonacci: Genera los primeros n números de Fibonacci.

let n = 10;
let fibonacci = [];
fibonacci[0] = 0;
fibonacci[1] = 1;
for (let i = 2; i < n; i++) {
    fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
}
console.log(fibonacci);