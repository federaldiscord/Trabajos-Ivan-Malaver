// 5 ejercicios for con 5 operadores ternarios con 5 if usables entre ellos

// Ejercicio 1
let porcentaje_batería = 15
let estado_bat = porcentaje_batería >20 ? "Batería baja" : "Batería suficiente"
console.log(estado_bat)

if (estado_bat === "Batería baja") {
    console.log("Conecte el cargador")
} else {
    console.log("Batería en buen estado")
}
for (let i = 0; i < 5; i++) {
    console.log(estado_bat)
    if (estado_bat === "Batería baja") {
        console.log("Conecte el cargador")
    } else {
        console.log("Batería en buen estado")
    }
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
for (let i = 0; i < 5; i++) {
    console.log(estado_accesorios)
    if (estado_accesorios === "Muchos accesorios") {
        console.log("Revisar accesorios")
    } else {
        console.log("Accesorios en buen estado")
    }
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
for (let i = 0; i < 5; i++) {
    console.log(estado_software)
    if (estado_software === "Software desactualizado") {
        console.log("Actualizar software")
    } else {
        console.log("Software en buen estado")
    }
}

// Ejercicio 4
let nivel_senal = 4
let estado_senal = nivel_senal >= 5 ? "Señal buena" : "Señal débil"
console.log(estado_senal)

if (estado_senal === "Señal débil") {
    console.log("Buscar mejor ubicación")
} else {
    console.log("Señal en buen estado")
}
for (let i = 0; i < 5; i++) {
    console.log(estado_senal)
    if (estado_senal === "Señal débil") {
        console.log("Buscar mejor ubicación")
    } else {
        console.log("Señal en buen estado")
    }
}

// Ejercicio 5
let temperatura = 30
if (temperatura > 30) {
    console.log("Temperatura alta")
} else if (temperatura <= 15) {
    console.log("Temperatura baja")
} else {
    console.log("Temperatura normal")
}
for (let i = 0; i < 5; i++) {
    console.log(temperatura)
    if (temperatura > 30) {
        console.log("Temperatura alta")
    } else if (temperatura <= 15) {
        console.log("Temperatura baja")
    } else {
        console.log("Temperatura normal")
    }
}