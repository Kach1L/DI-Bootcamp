const fs = require('fs');

function readFileContent() {
  try {
    const content = fs.readFileSync('./files/file-data.txt', 'utf8');
    
    console.log('File Content:');
    console.log(content);
  } catch (error) {
    console.error('Error reading file:', error);
  }
}

module.exports = readFileContent;
