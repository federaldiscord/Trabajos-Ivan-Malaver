// Sistema de Nómina: Calcula pagos según tipo de contrato.

let tipoContrato = prompt("Ingrese el tipo de contrato (A, B, C):");

let pago;

switch (tipoContrato) {
    case "A":
        pago = 1450000;
        break;
    case "B":
        pago = 1500000;
        break;
    case "C":
        pago = 2000000;
        break;
    default:
        console.log("Tipo de contrato inválido.");
        break;
}

if (pago !== undefined) {
    console.log(`El pago es: $${pago}`);
}