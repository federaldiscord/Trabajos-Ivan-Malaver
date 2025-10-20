// Formateador de Fechas: Convierte fechas entre diferentes formatos.
function formatearFecha(fecha, formato) {
    const date = (fecha instanceof Date) ? fecha : new Date(fecha);
    if (isNaN(date)) return "Fecha inválida";

    const dia = String(date.getDate()).padStart(2, "0");
    const mes = String(date.getMonth() + 1).padStart(2, "0");
    const anio = date.getFullYear();
    const hora = String(date.getHours()).padStart(2, "0");
    const minutos = String(date.getMinutes()).padStart(2, "0");

    const mesesLargos = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];

    switch (formato) {
        case "DD-MM-YYYY":
        return `${dia}-${mes}-${anio}`;
        case "MM/DD/YYYY":
        return `${mes}/${dia}/${anio}`;
        case "YYYY/MM/DD":
        return `${anio}/${mes}/${dia}`;
        case "LARGO":
        return `${dia} de ${mesesLargos[date.getMonth()]} de ${anio}`;
        case "DD/MM/YYYY HH:mm":
        return `${dia}/${mes}/${anio} ${hora}:${minutos}`;
        default:
        return "Formato no soportado";
    }
}
