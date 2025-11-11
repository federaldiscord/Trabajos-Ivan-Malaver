// Ejercicio 8:
let numero2 = prompt("Ingresa un número:");
let numero3 = Number(numero2);
if (isNaN(numero3)) {
    alert("El número ingresado no es válido.");
} else {
    if (numero3 % 2 === 0) {
        alert("El número " + numero3 + " es par.");
    } else {
        alert("El número " + numero3 + " es impar.");
    }
}