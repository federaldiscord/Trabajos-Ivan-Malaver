// Calculadora de Velocidad: Calcula velocidad, distancia o tiempo según los datos.

let opcion = parseInt(prompt("Ingrese el tipo de dato (1: Velocidad, 2: Distancia, 3: Tiempo):"));
let valor = parseFloat(prompt("Ingrese el valor:"));

if (opcion === 1) {
    let distancia = parseFloat(prompt("Ingrese la distancia recorrida:"));
    let tiempo = parseFloat(prompt("Ingrese el tiempo transcurrido en horas:"));
    let velocidad = distancia / tiempo;
    console.log(`La velocidad es: ${velocidad} m/s`);
} else if (opcion === 2) {
    let velocidad = parseFloat(prompt("Ingrese la velocidad en m/s:"));
    let tiempo = parseFloat(prompt("Ingrese el tiempo transcurrido en horas:"));
    let distancia = velocidad * tiempo;
    console.log(`La distancia recorrida es: ${distancia} m`);
} else if (opcion === 3) {
    let velocidad = parseFloat(prompt("Ingrese la velocidad en m/s:"));
    let distancia = parseFloat(prompt("Ingrese la distancia recorrida:"));
    let tiempo = distancia / velocidad;
    console.log(`El tiempo transcurrido es: ${tiempo} horas`);
} else {
    console.log("Opci&oacute;n inv&aacute;lida");
}