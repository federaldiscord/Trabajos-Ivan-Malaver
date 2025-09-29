// Calculadora de Calorías: Calcula calorías según actividad física y tiempo.

let opcion = parseInt(
    prompt("Ingrese el tipo de dato a calcular:\n1: Calorías\n2: Actividad física\n3: Tiempo")
);

let valor = parseFloat(prompt("Ingrese el valor:"));

let resultado;

switch (opcion) {
    case 1:
        resultado = valor * 60 * 60;
        console.log(`Las calorías son: ${resultado}`);
        break;
    case 2:
        resultado = valor * 60;
        console.log(`Las actividades fisicas son: ${resultado}`);
        break;
    case 3:
        resultado = valor;
        console.log(`Los tiempos son: ${resultado}`);
        break;
    default:
        console.log("Opción inválida.");
        break;
}