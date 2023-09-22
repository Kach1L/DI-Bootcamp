const chalk = require('chalk');

const colorfulMessage = chalk.bold.green('Hello, Chalk!') + ' ' + chalk.blue('This text is blue.') + ' ' + chalk.red('And this text is red.');

console.log(colorfulMessage);
