// Generador de Reportes: Función que genera reportes desde datos.

const datos = [
    { nombre: "Juan", ventas: 1200, zona: "Norte" },
    { nombre: "Ana", ventas: 1500, zona: "Sur" },
    { nombre: "Pedro", ventas: 800, zona: "Este" }
];

function generarReporte(datos, formato = "texto") {
    if (!Array.isArray(datos) || datos.length === 0) {
        return "No hay datos disponibles";
    }

    switch (formato) {
        case "texto":
        return datos
            .map(item => `Empleado: ${item.nombre} | Ventas: $${item.ventas} | Zona: ${item.zona}`)
            .join("\n");

        case "tabla":
        console.table(datos);
        return "Tabla generada en consola";

        case "csv":
        const encabezados = Object.keys(datos[0]).join(",");
        const filas = datos.map(item => Object.values(item).join(",")).join("\n");
        return encabezados + "\n" + filas;

        case "json":
        return JSON.stringify(datos, null, 2);

        default:
        return "Formato no soportado";
    }
}

console.log(generarReporte(datos, "texto"));
generarReporte(datos, "tabla");
console.log(generarReporte(datos, "csv"));
