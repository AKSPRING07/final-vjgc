const http = require("http");
const fs = require("fs");
const path = require("path");

const host = "127.0.0.1";
const port = 8000;
const root = path.join(__dirname, "public");

const mime = {
  ".css": "text/css; charset=utf-8",
  ".eot": "application/vnd.ms-fontobject",
  ".gif": "image/gif",
  ".html": "text/html; charset=utf-8",
  ".jpeg": "image/jpeg",
  ".jpg": "image/jpeg",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".map": "application/json; charset=utf-8",
  ".png": "image/png",
  ".svg": "image/svg+xml",
  ".ttf": "font/ttf",
  ".webp": "image/webp",
  ".woff": "font/woff",
  ".woff2": "font/woff2",
};

function send(res, status, body, contentType = "text/plain; charset=utf-8") {
  res.writeHead(status, { "Content-Type": contentType });
  res.end(body);
}

const server = http.createServer((req, res) => {
  const requestPath = decodeURIComponent((req.url || "/").split("?")[0]);
  const normalizedPath = path.normalize(requestPath).replace(/^(\.\.[\\/])+/, "");
  const relativePath =
    normalizedPath === "/" || normalizedPath === path.sep
      ? "index.html"
      : normalizedPath.replace(/^[\\/]/, "");

  const filePath = path.join(root, relativePath);

  if (!filePath.startsWith(root)) {
    send(res, 403, "Forbidden");
    return;
  }

  fs.stat(filePath, (statError, stats) => {
    if (statError) {
      send(res, 404, "Not Found");
      return;
    }

    const finalPath = stats.isDirectory() ? path.join(filePath, "index.html") : filePath;

    fs.readFile(finalPath, (readError, data) => {
      if (readError) {
        send(res, 404, "Not Found");
        return;
      }

      const ext = path.extname(finalPath).toLowerCase();
      send(res, 200, data, mime[ext] || "application/octet-stream");
    });
  });
});

server.listen(port, host, () => {
  console.log(`Website running at http://${host}:${port}`);
});
