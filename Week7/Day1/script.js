//Function Decleration and Calling

// function greet() {
//   console.log("Welcome to the page");
// }

// greet();

//Parameters
// function greet(username, age) {
//   console.log(`Welcome to the page ${username} your age is ${age}`);
// }

// greet("Daniel123", 19);

// function calculate(x, y, z) {
//   console.log(x + y + z + "a");
// }

// calculate(1, 1, 1);

//Functions Default Value
// function greet(username, age = "yet to be shared") {
//   console.log(`Welcome to the page ${username} your age is ${age}`);
// }

// greet("Daniel123");

//GLOBAL/LOCAL VARIABLES SCOPES
// const greeting = "hello";

// function userMoreInfo(userName, userAge) {
//   let eyeColor = "blue"; //local variable
//   console.log(`My name is ${userName} my age is ${userAge} and my eye color is ${eyeColor}`);
//   function randomFunc() {
//     console.log(eyeColor);
//   }
//   randomFunc();
// }

// userMoreInfo("Daniel", 26);

//Exercise
// function age(myAge) {
//   console.log(`The age of my mom is ${myAge * 2} the age of my dad is ${myAge * 2 * 1.2}`);
// }
// age(26);

//Return
// function calculate(x, y) {
//   let mySum = x + y;
//   //   console.log(mySum);
//   console.log("before return");

//   return mySum;
//   console.log("after return");
// }
// let sum = calculate(1, 2);
// console.log(sum);

//TRY CATCH ERRORS

// function exceptions() {
//   try {
//     console.log(helloIwillBeAneRROR);
//   } catch (e) {
//     console.log(e.name);
//     console.log(e.message);
//     console.log(e.stack);
//   } finally {
//     console.log("I will run in any case");
//   }
// }

// exceptions();

//Throw new error
// function calc(x, y) {
//   const sum = x + y;
//   try {
//     if (sum > 10) {
//       throw new Error("Your Number was bigger than allowed , Shutting down goodbye");
//     } else {
//       console.log(sum);
//     }
//   } catch (e) {
//     console.log(e);
//   }
// }
// calc(11, 2);

//Objects

// const person = {
//   fname: "Daniel",
//   lname: "Robin",
//   eat: function () {
//     console.log(`I love chocolate and my name is ${this.fname}`);
//   },
// };

// // console.log(person.lname);
// person.eat();
