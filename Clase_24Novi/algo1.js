const http = require(`http`)
const server = http.createServer((req , res) => {
    res.statusCode = 200;
    res.setHeader(`content-type`, `text/plain`);
    res.write(`El primer texto del servidor \n`);
    res.end(`aquí termina mi información`)
});

    const port = 3000;
    server.listen(port ,() => {
        console.log(`El servidor está corriendo http://localhost:${port}/`)
    }
);