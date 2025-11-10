class Motor {
    encender() {
        console.log("Encendido");
    }
}

class Carro {
    constructor(marca) {
        this.marca = marca;
        this.motor = new Motor();
    }

    arrancar() {
        console.log("Encendiendo" + this.marca + "..");
        this.motor.encender();
    }
}

const elCarro = new Carro("Audi");
elCarro.arrancar();