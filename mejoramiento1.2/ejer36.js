import fs from 'fs';

const contenido = fs.readFileSync('datos.txt', 'utf-8');
console.log('Contenido:', contenido);
