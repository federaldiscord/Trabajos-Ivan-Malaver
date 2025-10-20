// conversor_unidades.js

let opcion = parseInt(
    prompt("Ingrese el tipo de unidad:\n1: Kilómetros\n2: Metros\n3: Centímetros")
);

switch (opcion) {
    case 1: {
        let kilometros = parseFloat(prompt("Ingrese la cantidad en kilómetros:"));
        let metros = kilometros * 1000;
        let centimetros = metros * 100;
        console.log(`La cantidad en metros es: ${metros}`);
        console.log(`La cantidad en centímetros es: ${centimetros}`);
        break;
    }

    case 2: {
        let metros = parseFloat(prompt("Ingrese la cantidad en metros:"));
        let kilometros = metros / 1000;
        let centimetros = metros * 100;
        console.log(`La cantidad en kilómetros es: ${kilometros}`);
        console.log(`La cantidad en centímetros es: ${centimetros}`);
        break;
    }

    case 3: {
        let centimetros = parseFloat(prompt("Ingrese la cantidad en centímetros:"));
        let metros = centimetros / 100;
        let kilometros = metros / 1000;
        console.log(`La cantidad en kilómetros es: ${kilometros}`);
        console.log(`La cantidad en metros es: ${metros}`);
        break;
    }

    default:
        console.log("Opción inválida.");
}
