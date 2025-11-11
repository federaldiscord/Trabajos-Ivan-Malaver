const fs = require("fs");

const cliente = "Juan Pérez";
const producto = "Teclado mecánico";
const cantidad = 2;
const precioUnitario = 45.00;
const subtotal = cantidad * precioUnitario;
const iva = subtotal * 0.21;
const total = subtotal + iva;

const nuevoContenido = "Los datos de tu factura son: "



const ARCHIVO_DATO = "factura.txt";

fs.writeFile(ARCHIVO_DATO, nuevoContenido, (error) => {
    if (error) {
        console.error("Error al crear la factura:", error);
    } else {
        console.log("Factura generada correctamente:", ARCHIVO_DATO);
    }
});
