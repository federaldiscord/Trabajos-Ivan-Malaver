import fs from 'fs';

fs.appendFileSync('datos.txt', '\nNueva línea agregada.');
console.log('Archivo actualizado.');
