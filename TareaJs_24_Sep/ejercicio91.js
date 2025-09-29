// Conversor de Bases con Funciones: Convierte entre bases numéricas.

function convertirBase(numero, baseOrigen, baseDestino) {
    const decimal = parseInt(numero, baseOrigen);
    if (isNaN(decimal)) return "Número o base inválida";

    return decimal.toString(baseDestino).toUpperCase();
}

console.log(convertirBase("1010", 2, 10));
console.log(convertirBase("FF", 16, 2));
console.log(convertirBase("77", 8, 16));
console.log(convertirBase("255", 10, 2));
