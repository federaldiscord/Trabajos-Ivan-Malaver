let precios = [5, 10, 15, 20, 25];

precios.push(30);
precios.pop();

let filtrados = precios.filter(p => p > 10);

let conIVA = filtrados.map(p => p * 1.21);

console.log("Precios originales:", precios);
console.log("Filtrados (>10):", filtrados);
console.log("Con IVA:", conIVA);
