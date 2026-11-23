import { cp, mkdir, rm, stat } from 'node:fs/promises';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(fileURLToPath(new URL('..', import.meta.url)));
const output = resolve(root, 'dist');
const files = [
  'index.html',
  'course-enhancements.css',
  'course-enhancements.js',
  'github-credit.js',
  'lesson-content-en.js',
  'assets'
];

await rm(output, { recursive: true, force: true });
await mkdir(output, { recursive: true });

for (const file of files) {
  const source = resolve(root, file);
  const info = await stat(source).catch(() => null);
  if (!info) throw new Error(`Required deployment file is missing: ${file}`);
  await cp(source, resolve(output, file), { recursive: true });
}

console.log(`Built static site in ${output}`);
