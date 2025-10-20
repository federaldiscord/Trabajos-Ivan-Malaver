// Calculadora de Interés Simple: Calcula interés, capital, tiempo o tasa.

/*
Calculadora de Interés Simple
Fórmulas:
  - Interés = Capital * (Tasa/100) * Tiempo
  - Capital = Interés / ( (Tasa/100) * Tiempo )
  - Tiempo  = Interés / ( Capital * (Tasa/100) )
  - Tasa    = (Interés / (Capital * Tiempo)) * 100
*/

let opcion = parseInt(
    prompt("Ingrese el tipo de dato a calcular:\n1: Interés\n2: Capital\n3: Tiempo\n4: Tasa")
);

switch (opcion) {
    case 1: {
        let capital = parseFloat(prompt("Ingrese el capital invertido:"));
        let tiempo = parseFloat(prompt("Ingrese el tiempo en años:"));
        let tasa = parseFloat(prompt("Ingrese la tasa de interés anual (%):"));
        let interes = capital * (tasa / 100) * tiempo;
        console.log(`El interés es: ${interes.toFixed(2)}`);
        break;
    }

    case 2: { 
        let interes = parseFloat(prompt("Ingrese el interés:"));
        let tiempo = parseFloat(prompt("Ingrese el tiempo en años:"));
        let tasa = parseFloat(prompt("Ingrese la tasa de interés anual (%):"));
        let capital = interes / ((tasa / 100) * tiempo);
        console.log(`El capital invertido es: ${capital.toFixed(2)}`);
        break;
    }

    case 3: {
        let interes = parseFloat(prompt("Ingrese el interés:"));
        let capital = parseFloat(prompt("Ingrese el capital invertido:"));
        let tasa = parseFloat(prompt("Ingrese la tasa de interés anual (%):"));
        let tiempo = interes / (capital * (tasa / 100));
        console.log(`El tiempo en años es: ${tiempo.toFixed(2)}`);
        break;
    }

    case 4: {
        let interes = parseFloat(prompt("Ingrese el interés:"));
        let capital = parseFloat(prompt("Ingrese el capital invertido:"));
        let tiempo = parseFloat(prompt("Ingrese el tiempo en años:"));
        let tasa = (interes / (capital * tiempo)) * 100;
        console.log(`La tasa de interés anual es: ${tasa.toFixed(2)}%`);
        break;
    }

    default:
        console.log("Opción inválida.");
}
