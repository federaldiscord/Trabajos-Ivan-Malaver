// Map de Array: Transforma cada elemento de un array según una función.

function agregarEstado(personas) {
    return personas.map(persona => ({ ...persona, activo: true }));
}

const personas = [
    { nombre: "Ana", edad: 20 },
    { nombre: "Luis", edad: 25 }
];

console.log(agregarEstado(personas));
