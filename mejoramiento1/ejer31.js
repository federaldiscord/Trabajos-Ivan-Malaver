export class Persona {
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    presentarse() {
        console.log(`Hola, soy ${this.nombre} y tengo ${this.edad} años.`);
    }
}
