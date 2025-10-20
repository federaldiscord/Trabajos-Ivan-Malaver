// Calculadora Básica: Crea un programa que reciba dos números y muestre la suma, resta, multiplicación y división.

function sumar(a, b) {
        return a + b;
    }
    
    function restar(a, b) {
        return a - b;
    }
    
    function multiplicar(a, b) {
        return a * b;
    }
    
    function dividir(a, b) {
        if (b === 0) {
            return "No se puede dividir por cero.";
        }
        return a / b;
    }