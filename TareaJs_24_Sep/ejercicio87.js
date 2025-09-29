// Función Recursiva Fibonacci: Implementa Fibonacci de forma recursiva.

function fibonacci(n) {
    if (n < 0) return "Número inválido";
    if (n === 0) return 0;
    if (n === 1) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(fibonacci(6));
