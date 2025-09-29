// Formateador de Fechas: Convierte fechas entre diferentes formatos.
function formatearFecha(fecha, formato) {
    const date = new Date(fecha);
    if (isNaN(date)) return "Fecha inválida";

    const dia = String(date.getDate()).padStart(2, "0");
    const mes = String(date.getMonth() + 1).padStart(2, "0");
    const anio = date.getFullYear();

    switch (formato) {
        case "DD-MM-YYYY":
        return `${dia}-${mes}-${anio}`;
        case "MM/DD/YYYY":
        return `${mes}/${dia}/${anio}`;
        case "YYYY/MM/DD":
        return `${anio}/${mes}/${dia}`;
        case "LARGO":
        const meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];
        return `${dia} de ${meses[date.getMonth()]} de ${anio}`;
        default:
        return "Formato no soportado";
    }
}

console.log(formatearFecha("2025-09-28", "DD-MM-YYYY"));
console.log(formatearFecha("2025-09-28", "MM/DD/YYYY"));
console.log(formatearFecha("2025-09-28", "LARGO"));
