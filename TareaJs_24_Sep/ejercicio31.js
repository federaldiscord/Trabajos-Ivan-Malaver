// Calculadora de Impuestos: Calcula impuestos según diferentes rangos de ingresos.

let ingresos = parseFloat(prompt("Ingrese sus ingresos:"));

let impuesto;

if (ingresos <= 10000) {
    impuesto = 0;
} else if (ingresos <= 20000) {
    impuesto = 0.1;
} else {
    impuesto = 0.2;
}

let impuestoCalculado = ingresos * impuesto;
console.log(`El impuesto a pagar es: $${impuestoCalculado.toFixed(2)}`);