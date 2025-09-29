// Sistema de Autenticación: Función que simula login con validación.

const usuarios = [
    { username: "admin", password: "1234" },
    { username: "juan", password: "abcd" },
    { username: "maria", password: "pass2024" }
];

function login(username, password) {
    const usuarioEncontrado = usuarios.find(
        user => user.username === username && user.password === password
    );

    return usuarioEncontrado
        ? `✅ Acceso concedido. Bienvenido, ${username}!`
        : "❌ Usuario o contraseña incorrectos";
}

console.log(login("juan", "abcd"));
console.log(login("admin", "wrong"));
