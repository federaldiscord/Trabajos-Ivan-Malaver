const esMayorDeEdad = (edad) => {
    if (edad >= 18) {
        return "Eres mayor de edad.";
    } else {
        return "Eres menor de edad.";
    }
};

console.log(esMayorDeEdad(20));
console.log(esMayorDeEdad(15));
