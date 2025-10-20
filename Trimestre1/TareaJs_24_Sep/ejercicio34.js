// calculadora_cientifica_menu.js

    function raizCuadrada(num) {
    return Math.sqrt(num);
    }

    function potencia(base, exponente) {
    return Math.pow(base, exponente);
    }

    function logaritmoNatural(num) {
    return Math.log(num);
    }

    function logaritmoBase(num, base) {
    return Math.log(num) / Math.log(base);
    }

    let opcion = parseInt(
    prompt("Seleccione operación:\n1: Raíz cuadrada\n2: Potencia\n3: Logaritmo natural\n4: Logaritmo en base arbitraria")
    );

    switch (opcion) {
    case 1: {
        let num = parseFloat(prompt("Ingrese el número:"));
        console.log(`Raíz cuadrada de ${num} = ${raizCuadrada(num).toFixed(4)}`);
        break;
    }

    case 2: {
        let base = parseFloat(prompt("Ingrese la base:"));
        let exponente = parseFloat(prompt("Ingrese el exponente:"));
        console.log(`${base}^${exponente} = ${potencia(base, exponente).toFixed(4)}`);
        break;
    }

    case 3: {
        let num = parseFloat(prompt("Ingrese el número:"));
        console.log(`ln(${num}) = ${logaritmoNatural(num).toFixed(4)}`);
        break;
    }

    case 4: {
        let num = parseFloat(prompt("Ingrese el número:"));
        let base = parseFloat(prompt("Ingrese la base:"));
        console.log(`log base ${base} de ${num} = ${logaritmoBase(num, base).toFixed(4)}`);
        break;
    }

    default:
        console.log("Opción inválida.");
    }
