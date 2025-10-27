const http = require('http');
const fs = require('fs');

const PORT = process.env.PORT || 3000;
const API_URL = process.env.API_URL || '';

const server = http.createServer((req, res) => {
    fs.readFile('index.html', 'utf8', (err, html) => {
        if (err) {
            res.writeHead(500);
            res.end('Error loading index.html');
            return;
        }
        
        // Inject API_URL into HTML
        const htmlWithApi = html.replace(
            '{{API_URL}}',
            API_URL
        );
        
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(htmlWithApi);
    });
});

server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
    console.log(`API_URL configured: ${API_URL ? '✓' : '✗'}`);
});

