// Calculadora de Figuras: Calcula área y perímetro de diferentes figuras geométricas.

let opcion = parseInt(prompt("Ingrese el tipo de figura:\n1: Cuadrado\n2: Rectángulo\n3: Círculo"));

switch (opcion) {
    case 1:
        let lado = parseFloat(prompt("Ingrese el lado del cuadrado:"));
        let areaCuadrado = lado * lado;
        let perimetroCuadrado = 4 * lado;
        console.log(`Área del cuadrado: ${areaCuadrado}`);
        console.log(`Perímetro del cuadrado: ${perimetroCuadrado}`);
        break;
    case 2:
        let base = parseFloat(prompt("Ingrese la base del rectángulo:"));
        let altura = parseFloat(prompt("Ingrese la altura del rectángulo:"));
        let areaRectangulo = base * altura;
        let perimetroRectangulo = 2 * (base + altura);
        console.log(`Área del rectángulo: ${areaRectangulo}`);
        console.log(`Perímetro del rectángulo: ${perimetroRectangulo}`);
        break;
    case 3:
        let radio = parseFloat(prompt("Ingrese el radio del círculo:"));
        let areaCirculo = Math.PI * radio * radio;
        let perimetroCirculo = 2 * Math.PI * radio;
        console.log(`Área del círculo: ${areaCirculo}`);
        console.log(`Perímetro del círculo: ${perimetroCirculo}`);
        break;
    default:
        console.log("Opción inválida.");
        break;
}