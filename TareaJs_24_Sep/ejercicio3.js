// Mayor de Tres Números: Encuentra el mayor de tres números usando if-else.

let num1 = 10;
let num2 = 20;
let num3 = 30;

if (num1 > num2 && num1 > num3) {
    console.log(num1 + " es el mayor.");
} else if (num2 > num1 && num2 > num3) {
    console.log(num2 + " es el mayor.");
} else {
    console.log(num3 + " es el mayor.");
}