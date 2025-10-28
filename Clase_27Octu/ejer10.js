//Ejercicio switch con 5 casos
let num1 = 3;
let num2 = 2;
let operacion = 4;

switch (operacion) {
    case 1:
        console.log(num1 + num2);
        break;
    case 2:
        console.log(num1 - num2);
        break;
    case 3:
        console.log(num1 * num2);
        break;
    case 4:
        console.log(num1 / num2);
        break;
    default:
        console.log("Operación inválida.");
        break;
}