// Conversor de Moneda: Convierte entre diferentes monedas.

function convertirMoneda(cantidad, monedaOrigen, monedaDestino) {
    let tasaConversion = 0;
    if (monedaOrigen === "USD" && monedaDestino === "EUR") {
        tasaConversion = 0.85;
    } else if (monedaOrigen === "EUR" && monedaDestino === "USD") {
        tasaConversion = 1.15;
    } else if (monedaOrigen === "USD" && monedaDestino === "GBP") {
        tasaConversion = 0.72;
    } else if (monedaOrigen === "GBP" && monedaDestino === "USD") {
        tasaConversion = 1.39;
    } else if (monedaOrigen === "EUR" && monedaDestino === "GBP") {
        tasaConversion = 0.88;
    } else if (monedaOrigen === "GBP" && monedaDestino === "EUR") {
        tasaConversion = 1.12;
    }
    return cantidad * tasaConversion;
}