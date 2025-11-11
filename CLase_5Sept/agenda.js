    // Este será el archivo como principal, se llamarán otros archivos, según necesidad del usuario.
    import fs from 'fs';
    import readlineSync from 'readline-sync';
    import { crearArchivo } from './crear_Archivo.js';
    import { crearContacto } from './crear_Contacto.js';
    import { leerArchivo } from './leer_Archivo.js';
    import { borrarContacto } from './borrar_Contacto.js';

    const FILE_PATH = 'agenda.txt';

    function main() {
    console.log('=== Sistema de Agenda Telefónica ===\n');

    if (!fs.existsSync(FILE_PATH)) {
        const resp = readlineSync.question('No existe el archivo de agenda. ¿Desea crearlo? (s/n): ');
        if (resp.toLowerCase() === 's') {
        crearArchivo(FILE_PATH);
        console.log('Archivo creado correctamente.\n');
        } else {
        console.log('Debe existir un archivo de agenda para continuar.');
        return;
        }
    }

    let opcion;
    do {
        console.log('\nMenú principal:');
        console.log('1. Crear contacto');
        console.log('2. Borrar contacto');
        console.log('3. Ver contactos');
        console.log('4. Salir');
        opcion = readlineSync.question('Seleccione una opción: ');

        switch (opcion) {
        case '1':
            crearContacto(FILE_PATH);
            break;
        case '2':
            borrarContacto(FILE_PATH);
            break;
        case '3':
            leerArchivo(FILE_PATH);
            break;
        case '4':
            console.log('Saliendo...');
            break;
        default:
            console.log('Opción no válida.');
        }
    } while (opcion !== '4');
    }

    main();
