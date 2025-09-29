// Calculadora de Salario: Calcula salario según horas trabajadas y tipo de empleado.

let horasTrabajadas = parseFloat(prompt("Ingrese las horas trabajadas:"));
let tipoEmpleado = prompt("Ingrese el tipo de empleado (A, B, C):");

let salario;

switch (tipoEmpleado) {
    case "A":
        salario = horasTrabajadas * 10;
        break;
    case "B":
        salario = horasTrabajadas * 15;
        break;
    case "C":
        salario = horasTrabajadas * 20;
        break;
    default:
        console.log("Tipo de empleado inválido.");
        break;
}

if (salario !== undefined) {
    console.log(`El salario es: ${salario}`);
}