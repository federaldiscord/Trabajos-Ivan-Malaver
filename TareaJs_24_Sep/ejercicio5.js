// Conversor de Temperatura: Convierte de Celsius a Fahrenheit y viceversa.
function celsiusAFahrenheit(celsius) {
  return (celsius * 9/5) + 32;
}

function fahrenheitACelsius(fahrenheit) {
  return (fahrenheit - 32) * 5/9;
}

let celsiusInput = parseFloat(prompt("Ingrese la temperatura en Celsius:"));
let fahrenheitResult = celsiusAFahrenheit(celsiusInput);
console.log(`La temperatura en Fahrenheit es: ${fahrenheitResult.toFixed(2)}`);

let fahrenheitInput = parseFloat(prompt("Ingrese la temperatura en Fahrenheit:"));
let celsiusResult = fahrenheitACelsius(fahrenheitInput);
console.log(`La temperatura en Celsius es: ${celsiusResult.toFixed(2)}`);
