class Configuracion {
    constructor() {
        if (Configuracion._instancia) {
            return Configuracion._instancia;
        }
        this.modo = "oscuro";
        Configuracion._instancia = this;
    }
}

const config1 = new Configuracion();
const config2 = new Configuracion();

console.log(config1.modo);
console.log(config2.modo);