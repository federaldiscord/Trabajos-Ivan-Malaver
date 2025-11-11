// este será para ver los contactos guardados en el archivo agenda.txt
import fs from 'fs';

    export function leerArchivo(path) {
    const contenido = fs.readFileSync(path, 'utf-8');
    if (!contenido.trim()) {
        console.log('No hay contactos guardados.');
    } else {
        console.log('\n--- Contactos Guardados ---');
        console.log(contenido);
    }
    }
