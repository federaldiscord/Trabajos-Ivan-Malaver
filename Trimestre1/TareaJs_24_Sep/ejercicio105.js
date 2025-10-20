// Clasificación Edad: Clasifica por rangos de edad usando ternario.

const clasificarEdad = edad =>
    edad < 0 ? "Edad inválida" :
    edad < 12 ? "Niño" :
    edad < 18 ? "Adolescente" :
    edad < 60 ? "Adulto" :
    "Adulto Mayor";


console.log(clasificarEdad(5));
console.log(clasificarEdad(15));
console.log(clasificarEdad(30));
console.log(clasificarEdad(70));
console.log(clasificarEdad(-2));
