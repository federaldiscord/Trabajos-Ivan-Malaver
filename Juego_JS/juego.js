import { personajes, armaduras } from "./diccionarios.js";
import { opci_personaje, opci_armadura } from "./listas.js";
import { asciiPersonaje } from "./funciones.js";

    console.log("Bienvenido al combate por rondas orientado en RPG!");
    console.log("Recuerda que cada ronda puedes cambiar de personaje y armadura.\n");

    console.log("Elige tu personaje según quieras luchar esta ronda:");
    opci_personaje.forEach((op, i) => {
    console.log(`${i + 1}. ${personajes[op].nombre}`);
    });

    let personaje_idx = parseInt(prompt("Selecciona (1 o 2): ")) - 1;
    let personaje_elegido = personajes[opci_personaje[personaje_idx]];

    console.log("\nElige tu armadura:");
    opci_armadura.forEach((op, i) => {
    console.log(`${i + 1}. ${armaduras[op].nombre}`);
    });

    let armaduras_elegidas = [];
    for (let i = 0; i < opci_armadura.length; i++) {
    let respuesta = prompt(`¿Quieres equipar ${armaduras[opci_armadura[i]].nombre}? (s/n): `);
    if (respuesta.toLowerCase() === "s") {
        armaduras_elegidas.push(armaduras[opci_armadura[i]]);
    }
    }

    console.log("\nTu personaje equipado:");
    asciiPersonaje(personaje_elegido, armaduras_elegidas);

    console.log("¡Que comience la batalla!");
