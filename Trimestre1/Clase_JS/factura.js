// Imprimir una factura simple en la consola usando JavaScript
var cliente = "Steban";
var producto = "Curso de JavaScript";
var precio = 29.99;
var cantidad = 1;
var total = precio * cantidad;

console.log("Factura de Compra");
console.log("Cliente: " + cliente);
console.log("Producto: " + producto);
console.log("Precio: $" + precio.toFixed(2));
console.log("Cantidad: " + cantidad);
console.log("Total: $" + total.toFixed(2));
len = console.log("-" * 24)
console.log("Gracias por su compra!");
