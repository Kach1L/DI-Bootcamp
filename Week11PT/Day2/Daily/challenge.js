const greet = require('./Task1/greeting');
const createColorfulMessage = require('./Task2/colorful-message');
const readFileContent = require('./Task3files/read-file');

const userName = 'Eve';

const greetingMessage = greet(userName);
console.log(greetingMessage);

createColorfulMessage();

readFileContent();
