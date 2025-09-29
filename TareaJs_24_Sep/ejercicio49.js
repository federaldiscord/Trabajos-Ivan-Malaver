// Inversor de Número: Invierte un número (123 → 321).

let num = 123;
let invertido = 0;
while (num > 0) {
    let digito = num % 10;
    invertido = invertido * 10 + digito;
    num = Math.floor(num / 10);
}
console.log(`El número invertido es: ${invertido}`);