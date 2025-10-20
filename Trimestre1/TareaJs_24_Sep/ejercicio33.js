// Conversor de Tiempo: Convierte entre segundos, minutos y horas.

let opcion = parseInt(prompt("Ingrese el tipo de dato a calcular:\n1: Segundos\n2: Minutos\n3: Horas"));

let valor = parseFloat(prompt("Ingrese el valor:"));

let resultado;

switch (opcion) {
    case 1:
        resultado = valor * 60 * 60;
        console.log(`Los segundos son: ${resultado}`);
        break;
    case 2:
        resultado = valor * 60;
        console.log(`Los minutos son: ${resultado}`);
        break;
    case 3:
        resultado = valor;
        console.log(`Las horas son: ${resultado}`);
        break;
    default:
        console.log("Opción inválida.");
        break;
}