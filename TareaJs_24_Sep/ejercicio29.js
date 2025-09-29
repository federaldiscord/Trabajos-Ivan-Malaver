// 29.Sistema de Descuentos: Aplica descuentos diferentes según categoría de cliente.

let categoria = prompt("Ingrese la categoría del cliente (A, B, C):");

let descuento;

switch (categoria) {
    case "A":
        descuento = 10;
        break;
    case "B":
        descuento = 15;
        break;
    case "C":
        descuento = 20;
        break;
    default:
        console.log("Categoría inválida.");
        break;
}

if (descuento !== undefined) {
    let precio = 100;
    let precioConDescuento = precio * (1 - descuento / 100);
    console.log(`El precio con descuento es: $${precioConDescuento.toFixed(2)}`);
}
