export function obtenerPersonajes() {
    return [
        { nombre: "Hombre", ascii: "  O  \n /|\\ \n / \\ " },
        { nombre: "Mujer", ascii: "  O  \n /|\\ \n / \\ " },
    ];
    }

    export function obtenerArmaduras() {
    return [
        { nombre: "Casco", ascii: "  ^  " },
        { nombre: "Peto", ascii: " /|\\ " },
        { nombre: "Pantalón", ascii: "  |  " },
        { nombre: "Botas", ascii: " / \\ " },
    ];
    }

    export function asciiPersonaje(personaje, armaduras) {
    console.log(personaje.ascii);
    armaduras.forEach(a => console.log(a.ascii));
    }
