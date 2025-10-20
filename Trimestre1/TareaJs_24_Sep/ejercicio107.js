// Día Laboral: Determina si un día es laboral o fin de semana.

function diaLaboral(dia) {
    if (!dia) return "Día inválido";

    const diaNormalizado = dia.toLowerCase();

    return ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes"].includes(diaNormalizado)
        ? "Laboral"
        : ["sábado", "sabado", "domingo"].includes(diaNormalizado)
        ? "Fin de semana"
        : "Día no reconocido";
}

console.log(diaLaboral("Lunes"));
console.log(diaLaboral("sábado"));
console.log(diaLaboral("DOMINGO"));
console.log(diaLaboral("Feriado"));
