class CuentaBanco:
    """Clase que modela una cuenta bancaria básica."""

    def __init__(self, saldo_inicial: float = 0.0):
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.__saldo = saldo_inicial

    def depositar(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self.__saldo += monto

    def retirar(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes.")
        self.__saldo -= monto

    def consultar_saldo(self) -> float:
        return self.__saldo


if __name__ == "__main__":
    cuenta = CuentaBanco(1000)
    cuenta.depositar(500)
    print("Saldo después de depósito:", cuenta.consultar_saldo())
    cuenta.retirar(300)
    print("Saldo después de retiro:", cuenta.consultar_saldo())
