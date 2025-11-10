import fs from 'fs';

if (fs.existsSync('datos.txt')) {
    fs.unlinkSync('datos.txt');
    console.log('Archivo eliminado.');
} else {
    console.log('El archivo no existe.');
}
