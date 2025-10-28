//switch

let diaDeSemana = 3;
let nombreDia;

switch (diaDeSemana) {
    case 1:
        nombreDia = "Lunes";
        break;
    case 2:
        nombreDia = "Martes";
        break;
    default:
        nombreDia = "Otro día";
        break;
}

console.log(`Hoy es ${nombreDia}`);