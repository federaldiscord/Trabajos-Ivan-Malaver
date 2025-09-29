// Signo de Número: Determina si es positivo, negativo o cero.

function signoNumero(num) {
    if (num > 0) {
        return "Positivo";
    } else if (num < 0) {
        return "Negativo";
    } else {
        return "Cero";
    }
}

console.log(signoNumero(10));
console.log(signoNumero(-5));
console.log(signoNumero(0));
