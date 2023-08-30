// 

const pricesFruits = {
    apple : 2,
    pear : 3,
    banana : 1,
}

// I want to ask the user for a fruit
const userChoice = prompt("what fruit").toLowerCase();
// APPLE //Apple //APlPl
//banana

// dot notation doesnt work when we use variable
// const specificPrice = pricesFruits.userChoice;
// console.log(specificPrice);


const specificPrice = pricesFruits[userChoice];
//                     //pricesFruits["banana"];
console.log(specificPrice);