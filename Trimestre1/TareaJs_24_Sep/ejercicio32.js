// Sistema de Transporte: Calcula tarifas según medio de transporte y distancia.

let medioTransporte = prompt("Ingrese el medio de transporte (A, B, C):");
let distancia = parseFloat(prompt("Ingrese la distancia recorrida en km:"));

let tarifa;

switch (medioTransporte) {
    case "A":
        tarifa = distancia * 0.5;
        break;
    case "B":
        tarifa = distancia * 0.7;
        break;
    case "C":
        tarifa = distancia * 0.9;
        break;
    default:
        console.log("Medio de transporte inválido.");
        break;
}

if (tarifa !== undefined) {
    console.log(`La tarifa es: $${tarifa.toFixed(2)}`);
}