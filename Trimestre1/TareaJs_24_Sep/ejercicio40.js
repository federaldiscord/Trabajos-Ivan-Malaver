// Simulador de Cajero Automático: Simula operaciones básicas de un cajero.

let saldo = 1000000;

console.log("Bienvenido al Cajero Automático");
console.log("1. Depositar");
console.log("2. Retirar");
console.log("3. Salir");

let opcion = parseInt(prompt("Seleccione una opción: "));

switch (opcion) {
    case 1:
        let cantidad = parseFloat(prompt("Ingrese la cantidad a depositar:"));
        saldo += cantidad;
        console.log(`Depósito de ${cantidad} realizado. Nuevo saldo: ${saldo}`);
        break;
    case 2:
        cantidad = parseFloat(prompt("Ingrese la cantidad a retirar:"));
        if (cantidad > saldo) {
            console.log("Saldo insuficiente.");
        } else {
            saldo -= cantidad;
            console.log(`Retiro de ${cantidad} realizado. Nuevo saldo: ${saldo}`);
        }
        break;
    case 3:
        console.log("Gracias por usar el Cajero Automático.");
        break;
    default:
        console.log("Opción inválida.");
        break;
}