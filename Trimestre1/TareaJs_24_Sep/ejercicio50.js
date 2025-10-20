// Palíndromo: Verifica si un número o palabra es palíndromo.

let num = 12321;
let numStr = num.toString();
let invertido = numStr.split("").reverse().join("");
if (numStr === invertido) {
    console.log(num + " es palíndromo.");
} else {
    console.log(num + " no es palíndromo.");
}