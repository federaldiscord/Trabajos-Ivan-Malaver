// Juego de Piedra, Papel o Tijera: Implementa el juego clásico.

let opciones = ["piedra", "papel", "tijera"];
let jugador1 = prompt("Ingrese su elección (piedra, papel o tijera):");
let jugador2 = prompt("Ingrese su elección (piedra, papel o tijera):");

let eleccionJugador1 = opciones.indexOf(jugador1.toLowerCase());
let eleccionJugador2 = opciones.indexOf(jugador2.toLowerCase());

if (eleccionJugador1 === -1 || eleccionJugador2 === -1) {
    console.log("Elección inválida.");
} else {
    if (eleccionJugador1 === eleccionJugador2) {
        console.log("Empate.");
    } else if (
        (eleccionJugador1 === 0 && eleccionJugador2 === 2) ||
        (eleccionJugador1 === 1 && eleccionJugador2 === 0) ||
        (eleccionJugador1 === 2 && eleccionJugador2 === 1)
    ) {
        console.log("Jugador 1 gana.");
    } else {
        console.log("Jugador 2 gana.");
    }
}