// Conversor de Bases: Convierte números entre binario, decimal y hexadecimal.

function binarioADecimal(binario) {
    return parseInt(binario, 2);
}

function decimalABinario(decimal) {
    return decimal.toString(2);
}

function decimalAHexadecimal(decimal) {
    return decimal.toString(16);
}