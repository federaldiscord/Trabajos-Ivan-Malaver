// Este archivo será para borrar un contacto
import fs from 'fs';
import readlineSync from 'readline-sync';

    export function borrarContacto(path) {
    const contenido = fs.readFileSync(path, 'utf-8').split('\n').filter(Boolean);
    if (contenido.length === 0) {
        console.log('No hay contactos para borrar.');
        return;
    }

    const nombre = readlineSync.question('Ingrese el nombre del contacto a borrar: ');
    const filtrados = contenido.filter(linea => !linea.toLowerCase().includes(nombre.toLowerCase()));

    if (filtrados.length === contenido.length) {
        console.log('Contacto no encontrado.');
    } else {
        fs.writeFileSync(path, filtrados.join('\n') + '\n', 'utf-8');
        console.log(`Contacto "${nombre}" eliminado correctamente.`);
    }
    }
