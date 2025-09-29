// Calculadora Científica: Funciones trigonométricas, logaritmos, etc.

const CalculadoraCientifica = {
  // Operaciones básicas
    suma: (a, b) => a + b,
    resta: (a, b) => a - b,
    multiplicar: (a, b) => a * b,
    dividir: (a, b) => (b !== 0 ? a / b : "Error: división por cero"),

  // Potencias y raíces
    potencia: (a, b) => Math.pow(a, b),
    raizCuadrada: (a) => (a >= 0 ? Math.sqrt(a) : "Error: raíz negativa"),

  // Logaritmos
    log: (a) => (a > 0 ? Math.log10(a) : "Error: log inválido"),
    ln: (a) => (a > 0 ? Math.log(a) : "Error: ln inválido"),

  // Trigonometría (en radianes)
    seno: (a) => Math.sin(a),
    coseno: (a) => Math.cos(a),
    tangente: (a) => Math.tan(a),

  // Trigonometría inversa
    arcsin: (a) => Math.asin(a),
    arccos: (a) => Math.acos(a),
    arctan: (a) => Math.atan(a),

  // Constantes
    pi: () => Math.PI,
    e: () => Math.E
};

// Ejemplos de uso:
console.log("Suma:", CalculadoraCientifica.suma(5, 3));
console.log("Cos(π/3):", CalculadoraCientifica.coseno(Math.PI/3));
console.log("Ln(e):", CalculadoraCientifica.ln(Math.E));
