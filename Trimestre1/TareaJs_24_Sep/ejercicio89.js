// Manipulador de Strings: Función con diversas operaciones sobre strings.

function manipularString(cadena, operacion) {
    switch (operacion) {
        case "mayusculas":
        return cadena.toUpperCase();
        case "minusculas":
        return cadena.toLowerCase();
        case "invertir":
        return cadena.split("").reverse().join("");
        case "contarVocales":
        return (cadena.match(/[aeiouáéíóú]/gi) || []).length;
        case "sinEspacios":
        return cadena.replace(/\s+/g, "");
        case "capitalizar":
        return cadena
            .toLowerCase()
            .replace(/\b\w/g, letra => letra.toUpperCase());
        case "palabras":
        return cadena.trim().split(/\s+/); // Devuelve array de palabras
        default:
        return "Operación no soportada";
    }
}

console.log(manipularString("Hola Mundo", "mayusculas"));
console.log(manipularString("Hola Mundo", "invertir"));
console.log(manipularString("Hola Mundo", "contarVocales"));
console.log(manipularString("hola  mundo ", "palabras"));
