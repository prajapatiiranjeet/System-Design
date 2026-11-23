import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { extname, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(fileURLToPath(new URL('.', import.meta.url)));
const port = Number(process.env.PORT || 5173);
const types = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.woff2': 'font/woff2',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.webp': 'image/webp'
};

const server = createServer(async (req, res) => {
  if (!['GET', 'HEAD'].includes(req.method || '')) {
    res.writeHead(405, { Allow: 'GET, HEAD' }).end('Method not allowed');
    return;
  }

  let pathname;
  try {
    pathname = decodeURIComponent(new URL(req.url || '/', 'http://localhost').pathname);
  } catch {
    res.writeHead(400).end('Bad request');
    return;
  }
  const requested = pathname === '/' ? '/index.html' : pathname;
  const target = resolve(root, `.${requested}`);
  if (target !== root && !target.startsWith(root + sep)) {
    res.writeHead(403).end('Forbidden');
    return;
  }

  try {
    const fileStat = await stat(target);
    if (!fileStat.isFile()) throw new Error('Not a file');
    const body = await readFile(target);
    res.writeHead(200, {
      'Content-Type': types[extname(target)] || 'application/octet-stream',
      'Content-Length': body.length,
      'X-Content-Type-Options': 'nosniff',
      'Cache-Control': 'no-cache'
    });
    res.end(req.method === 'HEAD' ? undefined : body);
  } catch {
    res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' }).end('Not found');
  }
});

server.listen(port, '127.0.0.1', () => {
  console.log(`System Design course is available at http://127.0.0.1:${port}`);
});
