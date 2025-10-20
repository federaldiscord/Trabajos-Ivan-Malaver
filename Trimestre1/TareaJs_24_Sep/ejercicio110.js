// Estado de Agua: Determina estado (sólido, líquido, gaseoso) por temperatura.

const estadoAgua = temp =>
    temp < 0 ? "Congelado" :
    temp < 100 ? "Líquido" :
    "Gaseoso (Vapor)";

console.log(estadoAgua(-5));
console.log(estadoAgua(25));
console.log(estadoAgua(120));
