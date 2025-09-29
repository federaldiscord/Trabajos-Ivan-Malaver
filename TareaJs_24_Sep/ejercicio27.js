// Menú de Restaurante: Simula un menú con diferentes opciones de comida.

let menu = `
    1. Ensalada
    2. Pollo
    3. Carne
    4. Postre
    5. Bebida
    6. Salir
    `;

console.log(menu);

let opcion = prompt("Selecciona una opció: ");

switch (opcion) {
    case "1":
        console.log("Has elegido la ensalada.");
        break;
    case "2":
        console.log("Has elegido el pollo.");
        break;
    case "3":
        console.log("Has elegido la carne.");
        break;
    case "4":
        console.log("Has elegido el postre.");
        break;
    case "5":
        console.log("Has elegido la bebida.");
        break;
    case "6":
        console.log("Has elegido salir.");
        break;
    default:
        console.log("Opci&oacute;n inv&aacute;lida.");
        break;
}