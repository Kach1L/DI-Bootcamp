import people from './data.js';

function calculateAverageAge(people) {
  const totalAge = people.reduce((sum, person) => sum + person.age, 0);
  return totalAge / people.length;
}

const averageAge = calculateAverageAge(people);
console.log(`The average age of all persons is: ${averageAge}`);

