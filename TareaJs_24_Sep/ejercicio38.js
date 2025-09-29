// Sistema de Puntos: Asigna puntos según compras y calcula beneficios.

let compra = parseFloat(prompt("Ingrese el valor de la compra:"));

let puntos;

if (compra >= 1000) {
    puntos = compra * 0.1;
    console.log(`Has ganado ${puntos} puntos.`);
}

if (compra >= 5000) {
    puntos = compra * 0.2;
    console.log(`Has ganado ${puntos} puntos.`);
}

if (compra >= 10000) {
    puntos = compra * 0.3;
    console.log(`Has ganado ${puntos} puntos.`);
}

if (compra >= 20000) {
    puntos = compra * 0.4;
    console.log(`Has ganado ${puntos} puntos.`);
}

if (compra >= 50000) {
    puntos = compra * 0.5;
    console.log(`Has ganado ${puntos} puntos.`);
}

if (compra >= 100000) {
    puntos = compra * 0.6;
    console.log(`Has ganado ${puntos} puntos.`);
}