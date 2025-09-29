// 45.Números Primos: Genera los primeros n números primos.

let n = prompt("Ingrese el valor de n:");
let primos = [];
for (let i = 2; primos.length < n; i++) {
    let esPrimo = true;
    for (let j = 2; j < i; j++) {
        if (i % j === 0) {
            esPrimo = false;
            break;
        }
    }
    if (esPrimo) {
        primos.push(i);
    }
}
console.log(primos);