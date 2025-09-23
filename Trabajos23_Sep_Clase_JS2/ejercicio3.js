// 5 ciclos y 5 operadores ternarios y que sean usables entre sí

// Ejercicio 1
let porcentaje_batería = 15
let estado_bat = porcentaje_batería >20 ? "Batería baja" : "Batería suficiente"
console.log(estado_bat)

if (estado_bat === "Batería baja") {
    console.log("Conecte el cargador")
} else {
    console.log("Batería en buen estado")
}

// Ejercicio 2
let cantidad_accesorios = 3
let estado_accesorios = cantidad_accesorios > 5 ? "Muchos accesorios" : "Pocos accesorios"
console.log(estado_accesorios)

if (estado_accesorios === "Muchos accesorios") {
    console.log("Revisar accesorios")
} else {
    console.log("Accesorios en buen estado")
}
// Ejercicio 3
let nivel_software = 4
let estado_software = nivel_software >= 5 ? "Software actualizado" : "Software desactualizado"
console.log(estado_software)

if (estado_software === "Software desactualizado") {
    console.log("Actualizar software")
} else {
    console.log("Software en buen estado")
}

// Ejercicio 4
let espacio_almacenamiento = 80
let estado_almacenamiento = espacio_almacenamiento > 90 ? "Almacenamiento casi lleno" : "Almacenamiento suficiente"
console.log(estado_almacenamiento)

if (estado_almacenamiento === "Almacenamiento casi lleno") {
    console.log("Liberar espacio")
} else {
    console.log("Almacenamiento en buen estado")
}

// Ejercicio 5
let nivel_senal = 3
let estado_senal = nivel_senal >= 4 ? "Buena señal" : "Señal débil"
console.log(estado_senal)

if (estado_senal === "Señal débil") {
    console.log("Buscar mejor ubicación")
} else {
    console.log("Señal en buen estado")
}