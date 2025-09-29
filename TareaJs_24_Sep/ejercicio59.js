// Números Perfectos: Encuentra números perfectos hasta un límite.

function esPerfecto(num) {
    let suma = 0;
    for (let i = 1; i < num; i++) {
        if (num % i === 0) {
        suma += i;
        }
    }
    return suma === num;
}

    function numerosPerfectosHasta(limite) {
    const perfectos = [];
    for (let i = 1; i <= limite; i++) {
        if (esPerfecto(i)) {
        perfectos.push(i);
        }
    }
    return perfectos;
}

console.log("Números perfectos hasta 1000:", numerosPerfectosHasta(1000));
