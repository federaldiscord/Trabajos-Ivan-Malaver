// Sistema de Calificaciones: Convierte notas numéricas a letras (A, B, C, etc.).

let nota = 3.5;
let calificacion;

switch (true) {
    case nota >= 4.5:
        calificacion = "A";
        break;
    case nota >= 3.5:
        calificacion = "B";
        break;
    case nota >= 2.5:
        calificacion = "C";
        break;
    case nota >= 1.5:
        calificacion = "D";
        break;
    case nota >= 0:
        calificacion = "E";
        break;
    default:
        calificacion = "Nota inválida";
}

console.log(`La calificación es: ${calificacion}`);