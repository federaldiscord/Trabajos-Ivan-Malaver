function persona(nombre, apellido, edad) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.edad = edad;
}

persona.prototype.saludar = function() {
    console.log(`Hola, mi nombre es ${this.nombre} ${this.apellido} y tengo ${this.edad} años.`);
}

const persona1 = new persona("Juan", "Pérez", 30);
persona1.saludar();