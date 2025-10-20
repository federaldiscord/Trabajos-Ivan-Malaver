// Estación del Año: Determina la estación según el mes.

let mes = parseInt(prompt("Ingrese el número del mes (1-12):"));

switch (mes) {
    case 1:
    case 2:
    case 12:
        console.log("Invierno");
        break;
    case 3:
    case 4:
    case 5:
        console.log("Primavera");
        break;
    case 6:
    case 7:
    case 8:
        console.log("Verano");
        break;
    case 9:
    case 10:
    case 11:
        console.log("Otono");
        break;
    default:
        console.log("Mes inválido.");
        break;
}