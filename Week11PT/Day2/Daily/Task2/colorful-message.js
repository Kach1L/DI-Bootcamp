const chalk = require('chalk');

function createColorfulMessage() {
  const message = 'This is a colorful message!';
  const colorfulMessage = chalk.blue.bold(message);
  console.log(colorfulMessage);
}

module.exports = createColorfulMessage;
