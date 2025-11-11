let var1 = true;
let var2 = false;
let var3 = true;

if (var1 && var2 === true) {
    console.log("Las dos son verdaderas");
} else if (var1 || var2 === true) {
    console.log("Al menos una es verdadera");
} else if (var3 === false) {
    console.log("Ninguna es verdadera");
} else {
    console.log("La tercera es verdadera");
}