// Este archivo será para crear un nuevo contacto haciendo uso de su nombre, celular.
import fs from 'fs';
import readlineSync from 'readline-sync';

    export function crearContacto(path) {
        const nombre = readlineSync.question('Ingrese el nombre: ');
        const celular = readlineSync.question('Ingrese el número de celular: ');

        if (!nombre || !celular) {
            console.log('Error: nombre y celular son obligatorios.');
            return;
        }

        const nuevoContacto = `Nombre: ${nombre}, Celular: ${celular}\n`;
        fs.appendFileSync(path, nuevoContacto, 'utf-8');
        console.log('Contacto agregado exitosamente.');
    }
