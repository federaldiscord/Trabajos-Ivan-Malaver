// Función de Validación: Crea función que valide diferentes tipos de datos.

function validar(valor, tipo) {
    switch (tipo) {
        case "numero":
        return typeof valor === "number" && !isNaN(valor);

        case "string":
        return typeof valor === "string";

        case "boolean":
        return typeof valor === "boolean";

        case "email":
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(valor);

        case "telefono":
        return /^[0-9]{7,15}$/.test(valor);

        case "fecha":
        return !isNaN(Date.parse(valor));

        case "noVacio":
        return valor !== null && valor !== undefined && valor !== "";

        default:
        return false;
    }
}

console.log(validar(123, "numero"));
console.log(validar("hola", "string"));
console.log(validar("user@mail.com", "email"));
console.log(validar("1234567", "telefono"));
console.log(validar("2023-01-01", "fecha"));
console.log(validar("", "noVacio"));
