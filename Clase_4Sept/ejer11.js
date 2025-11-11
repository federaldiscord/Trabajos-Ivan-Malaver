const fs  = require ('fs');
const archivo_datos = "datos.txt";

fs.writeFile(archivo_datos, "Hola Yusepe",
    (err) => err? console.error(err):
    console.log("Archivo creado")
);