
const http = require("http");
const fs = require("fs");
const path = require("path");

const DATA_FILE = path.join(__dirname, "data.txt");

if (!fs.existsSync(DATA_FILE)) {
    fs.writeFileSync(DATA_FILE, "");
}

const server = http.createServer((req, res) => {
    res.setHeader("Content-Type", "application/json");

    if (req.method === "POST" && req.url === "/create") {
        let body = "";

        req.on("data", chunk => (body += chunk));

        req.on("end", () => {
            fs.appendFile(DATA_FILE, body + "\n", (err) => {
                if (err) return res.end(JSON.stringify({ error: "No se pudo guardar." }));
                res.end(JSON.stringify({ message: "Registro creado.", data: body }));
            });
        });

        return;
    }

    if (req.method === "GET" && req.url === "/read") {
        fs.readFile(DATA_FILE, "utf8", (err, data) => {
            if (err) return res.end(JSON.stringify({ error: "No se pudo leer el archivo." }));
            res.end(JSON.stringify({ data }));
        });

        return;
    }

    if (req.method === "PUT" && req.url === "/update") {
        let body = "";

        req.on("data", chunk => (body += chunk));

        req.on("end", () => {
            fs.writeFile(DATA_FILE, body, (err) => {
                if (err) return res.end(JSON.stringify({ error: "No se pudo actualizar." }));
                res.end(JSON.stringify({ message: "Archivo actualizado.", data: body }));
            });
        });

        return;
    }

    if (req.method === "DELETE" && req.url === "/delete") {
        fs.writeFile(DATA_FILE, "", (err) => {
            if (err) return res.end(JSON.stringify({ error: "No se pudo borrar." }));
            res.end(JSON.stringify({ message: "Archivo borrado." }));
        });

        return;
    }

    res.statusCode = 404;
    res.end(JSON.stringify({ error: "Ruta no encontrada." }));
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Servidor corriendo: http://localhost:${PORT}`);
});
