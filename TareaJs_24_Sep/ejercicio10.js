// Año Bisiesto: Verifica si un año es bisiesto.

let ano = 2000;
if (ano % 4 === 0) {
    if (ano % 100 === 0) {
        if (ano % 400 === 0) {
            console.log(ano + " es bisiesto.");
        } else {
            console.log(ano + " no es bisiesto.");
        }
    } else {
        console.log(ano + " es bisiesto.");
    }
} else {
    console.log(ano + " no es bisiesto.");
}