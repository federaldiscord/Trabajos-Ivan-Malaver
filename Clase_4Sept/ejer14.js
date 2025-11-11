const { isUtf8 } = require("buffer");
const { error } = require("console");
const fs = require("fs");

const archivo_datos = "datos.txt";
fs.readFile(archivo_datos, 'utf8', (errordatos)) => {
    if (error) {
        console.error("Error al leer ", error);
    }
}