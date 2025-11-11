class Persona {
    constructor(nombre, apellido, edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }

    saludar() {
        console.log(`Hola, mi nombre es ${this.nombre} ${this.apellido} y tengo ${this.edad} años.`);
    }
}

const persona1 = new Persona("Juan", "Pérez", 30);
persona1.saludar();