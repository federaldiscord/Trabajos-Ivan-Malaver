// ejer3.js
import promptSync from "prompt-sync";
const prompt = promptSync();

const numeroTexto = prompt("Escribe un número: ");
const numero = parseFloat(numeroTexto);

if (isNaN(numero)) {
    console.log("No escribiste un número válido.");
} else {
    console.log(`Escribiste el número ${numero}.`);
}
