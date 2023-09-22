const http = require("http");

const server = http.createServer((request, response) => {
    response.end("Hello from my first web server")
});

server.listen(5000);