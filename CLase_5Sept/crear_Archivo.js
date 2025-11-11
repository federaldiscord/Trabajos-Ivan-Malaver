// Con este se creará el archivo agenda.txt si no existe
import fs from 'fs';

    export function crearArchivo(path) {
    if (!fs.existsSync(path)) {
        fs.writeFileSync(path, '', 'utf-8');
    }
    }
