class cuentaBanc {
    constructor(saldoIni) {
        this._saldo = saldoIni;
    }

    get saldo() {
        return this._saldo;
    }

    set saldo(valor) {
        if (valor <= 0) {
            console.log("El saldo no puede ser negativo");
        } else {
            this._saldo = valor;
        }
    }
}

const cuenta = new cuentaBanc(1000000);
console.log(cuenta.saldo);
cuenta.saldo = 500000;
cuenta.saldo = -100000;
console.log(cuenta.saldo);