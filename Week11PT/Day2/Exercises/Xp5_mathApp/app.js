const _ = require('lodash');
const { add, multiply } = require('./math');

const result1 = add(5, 3);
const result2 = multiply(4, 6);
const result3 = _.sum([1, 2, 3, 4, 5]);

console.log('Result of addition:', result1);
console.log('Result of multiplication:', result2);
console.log('Result of lodash sum:', result3);
