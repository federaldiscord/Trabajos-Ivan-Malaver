const fs = require("fs");
const archivo_datos = "datos.txt";
fs.unlink(archivo_datos, (err)=>{
    if (err) throw err,
    console.log ("archivo eliminado")
});