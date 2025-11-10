class Animal {
    constructor(nombre) {
        this.nombre = nombre;
    }


    sonido() {
        console.log("El animal hace")
    }
}

class Perro extends Animal {
    constructor(nombre, raza) {
        super(nombre);
        this.raza = raza;
    }


    sonido() {
        console.log(this.nombre + " dice: ¡Guau!");
    }
}

const elPerro = new Perro("Pedro", "Perro de gato");
elPerro.sonido();