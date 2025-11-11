class persona {
    constructor(nombre, edad){
        this.nombre = nombre;
        this.edad = edad;
    }
    saludar(){
        console.log(`Hola, mi nombre es ${this.nombre} y tengo ${this.edad} años.`);
    }

    cumplirAnos() {
        this.edad ++;
    }
}

const persona1 = new persona("Carlos", 25);

console.log(persona1);
persona1.saludar();
persona1.cumplirAnos();
persona1.saludar();