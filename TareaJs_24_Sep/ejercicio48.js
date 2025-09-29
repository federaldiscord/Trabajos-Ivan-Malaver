// Contador de Vocales: Cuenta las vocales en una cadena de texto.

function contarVocales(texto) {
    texto = texto.toLowerCase();
    const vocales = "aeiouáéíóú";
    let contador = 0;

    for (let letra of texto) {
    if (vocales.includes(letra)) contador++;
    }

    return contador;
}

const entrada = prompt("Ingresa un texto para contar sus vocales:");
alert(`El texto tiene ${contarVocales(entrada)} vocales.`);
