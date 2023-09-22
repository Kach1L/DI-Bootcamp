const fs = require('fs');

function readFile(fileName) {
  try {
    return fs.readFileSync(fileName, 'utf8');
  } catch (error) {
    console.error(`Error reading file "${fileName}": ${error.message}`);
    return null;
  }
}

function writeFile(fileName, content) {
  try {
    fs.writeFileSync(fileName, content);
    console.log(`File "${fileName}" written successfully.`);
  } catch (error) {
    console.error(`Error writing to file "${fileName}": ${error.message}`);
  }
}

module.exports = {
  readFile,
  writeFile,
};
