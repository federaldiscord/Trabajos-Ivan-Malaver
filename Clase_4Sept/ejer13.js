const fs = require("fs");
fs.writeFile(ARCHIVO_DATO);
NuevoContenido, (error)=>{
    if (error){
        console.error('error', error);
    } else {
        console.log("Archivo editado");
    }
}