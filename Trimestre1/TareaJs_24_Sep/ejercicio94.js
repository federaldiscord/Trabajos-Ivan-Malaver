// Cifrado César: Implementa cifrado César para textos.

function cifradoCesar(texto, desplazamiento, descifrar = false) {
    if (descifrar) desplazamiento = -desplazamiento;

    return texto.replace(/[a-zñ]/gi, (letra) => {
        const esMayuscula = letra === letra.toUpperCase();
        const alfabeto = "abcdefghijklmnñopqrstuvwxyz";
        const letraMin = letra.toLowerCase();

        const indiceActual = alfabeto.indexOf(letraMin);
        if (indiceActual === -1) return letra;

        let nuevoIndice = (indiceActual + desplazamiento) % alfabeto.length;
        if (nuevoIndice < 0) nuevoIndice += alfabeto.length;

        const nuevaLetra = alfabeto[nuevoIndice];
        return esMayuscula ? nuevaLetra.toUpperCase() : nuevaLetra;
    });
}

console.log(cifradoCesar("Hola Mundo", 3));
console.log(cifradoCesar("Krod Pxqgr", 3, true));
