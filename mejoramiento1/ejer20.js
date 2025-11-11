const calificar = (nota) => {
    if (nota >= 90) {
        return "Excelente";
    } else if (nota >= 70) {
        return "Aprobado";
    } else {
        return "Reprobado";
    }
};

console.log(calificar(95));
console.log(calificar(75));
console.log(calificar(50));
