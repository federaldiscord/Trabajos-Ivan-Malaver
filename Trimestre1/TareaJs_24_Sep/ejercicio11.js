// Calculadora de Descuento: Aplica un descuento porcentual a un precio.

let precio = 100;
let descuento = 20;
let precioConDescuento = precio * (1 - descuento / 100);
console.log(`El precio con descuento es: $${precioConDescuento.toFixed(2)}`);