const { readFile, writeFile } = require('./fileManager.js');

const helloContent = readFile('Hello World.txt');

if (helloContent) {
  writeFile('Bye World.txt', 'Writing to the file');
}
