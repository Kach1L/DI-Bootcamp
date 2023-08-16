let veryImportantThing = 2;

//Console Log

// console.log("Hello World");
// console.log(
//   "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Magnam voluptas excepturi doloribus, ex, facilis aperiam ducimus ipsa liberoeius neque consequuntur placeat sequi repellendus possimus eum laborum veritatis? Culpa, quo."
// );

//Variables
// let x = 3;
// let X = 4;
// let my_name = "Daniel";
// let my_name2 = "Robin";
// // console.log(x + X);

// //Camel Case
// let myName = "Daniel";
// let thisIsMyName = "Daniel";

// //Undefined

// let a;
// console.log(a);

//Data types
//Strings
// let exampleString = "Hello";
// let exampleString2 = "World";
// console.log(exampleString + " " + exampleString2);
// console.log("2");

// let longString = "This is a very long string which needs \ to wrap across multiple lines because \ otherwise, my code is unreadable.";

// console.log(longString);

//String Properties and Methods
// let myName = "Daniel is a teacher";
// console.log(myName.length);

//Indexof
// console.log(myName.indexOf("a"));

//Substring
// console.log(myName.substring(7, 10));

//toLowerCase & toUpperCase
// let myString = "AbCdEfGhI";
// console.log(myString.toLowerCase());
// console.log(myString.toUpperCase());
// console.log(myString);

//Exercise 1
// let addressNumber = 1;
// let addressStreet = "Ben Yehuda";
// let country = "Israel";

// let globalAddress = addressStreet + " " + addressNumber + " in " + country;

// console.log("I live in " + globalAddress);

//Numbers
// console.log(10 / 2);
// console.log(10 - 2);
// console.log(10 * 2);

//Number Methods
//isNan
// let op = "2";
// console.log(isNaN(op));

//toString
// let ten = 10;
// console.log(ten);
// console.log(ten.toString());

//Comparison
// let x = 6;

//checks value- Regardless of type
// console.log(x == "2");
//checks value and type
// console.log(x === "2");
//not equal
// console.log(x != 2);
//greater than or equal
// console.log(x >= 2);
//check for two conditons
// console.log(x > 1 && x < 3);
// console.log(x > 5 || x === 2);

//Working with Numbers
// x++;
// console.log(x);

//User Interface Functions
//Alert
// console.log("Before alert");
// alert("Welcome to my website");
// console.log("After Alert");

//Prompt
// let userAnswer = prompt("What is your name?", "Guest");
// console.log("Welcome to the website " + userAnswer);

//Confirm
// let isBoss = confirm("Are you sure you want to delete this account?");
// alert(isBoss);

//Arrays
// let users = ["Daniel", "Alex", "Mikhael", "Kachi"];

// console.log(typeof users);

// console.log(users[0]);

// let colors = ["blue", "yellow", "green", 54];

// console.log(colors[3]);

// let arrayCeption = [
//   [1, 2, 3],
//   [5, 6, 7, 8],
//   [11, 13, 15],
// ];
// console.log(arrayCeption[0][1]);
// console.log(arrayCeption[2][2]);

// let colors = ["Pink", "Blue", "Green"];
// console.log(colors);
// colors[1] = "Yellow";
// console.log(colors);
// let arrayLength = colors.length;
// console.log(arrayLength);

//Array Methods
// let colors = ["Pink", "Blue", "Green"];
// console.log(colors);

// //add to end of array
// colors.push("Yellow");
// colors.push("Purple");
// console.log(colors);

// //remove from end of array
// colors.pop();
// colors.pop();

// console.log(colors);

//SPLICE ARRAY REMOVE/ADD ITEMS
// let colors = ["blue", "yellow", "green"];
// console.log(colors);
// colors.splice(1, 2, "grey");
// console.log(colors);

//Slice
// let colors = ["blue", "yellow", "green", "pink"];
// let slicedArray = colors.slice(1, 2);
// console.log(colors);
// console.log(slicedArray);

// console.log(colors.toString());

// let person = {
//   firstName: "Daniel",
//   lastName: "Robin",
//   age: 26,
//   eyeColor: "blue",
// };

// console.log(person.firstName);
// console.log(person.lastName);
// console.log(person.age);

//ADD OR CHANGE VALUES
// person.country = "Israel";
// console.log(person);
// person.age = 27;
// console.log(person);

//DELETE FROM OBJECT
// delete person.age;
// console.log(person);

//IF STATEMENTS- CONDITIONALS

// if ("condition === true"){
// "do this"
// }

// let x = 15;

// if (x >= 21) {
//   console.log("You can drink in the united states AND ANYWHERE ELSE");
// } else if (x === 18) {
//   console.log("You can drink in most places excluding the US");
// } else if (x >= 16 && x < 18) {
//   console.log("You can drink in Germany");
// } else {
//   console.log("You are too young to drink");
// }

//Exercise Keys Car

// let userAnswer = prompt("What is your age?");
// console.log(userAnswer);
// if (userAnswer == 18) {
//   alert("Mazal tov you can drive");
// } else if (userAnswer > 18) {
//   alert("You are over 18 you can drive ( and drink a bit)");
// } else {
//   alert("You are too young to drive");
// }

//Switch Case

// let fruit = "Apple";

// switch (fruit) {
//   case "Oranges":
//     console.log("Oranges are 0.6 per kilo");
//     break;
//   case "Mangoes":
//   case "Papayas":
//     console.log("Mangoes and Papayas are 2.5 per kilo");
//     break;
//   case "Apple":
//     console.log("apples are 1 per kg");
//     break;
//   default:
//     console.log("Sorry we are out of " + fruit);
// }

//LOOPS
//for loop

// for (let i = 0; i < 10; i++) {
//   console.log("the current number is " + i);
// }

//loop through an array
// let colors = ["red", "blue", "green", "purple", "pink", "grey"];
// console.log(colors[0]);

// for (let i = 0; i < colors.length; i++) {
//   console.log("the " + (i + 1) + " color is " + colors[i]);
// }

//LOOPS FOR/IN OBJECTS

// let person = {
//   name: "Daniel",
//   age: "26",
//   country: "Israel",
// };

// for (let key in person) {
//   console.log("The key is " + key + " and the value is " + person[key]);
// }

//LOOPS FOR/OF ARRAY
// let colors = ["blue", "yellow", "red", "pink"];

// for (let i of colors) {
//   console.log(i);
// }

//While Loop
// let n = 0;
// while (n < 3) {
//   console.log(n);
//   n++;
// }

// let answer = prompt("What is the secret password?");
// while (answer != "1234") {
//   answer = prompt("What is the secret password?");
// }
// alert("Welcome Admin");

//DO WHILE LOOP- will run at least once
// let i = 1;
// do {
//   console.log("The number is " + i);
//   i++;
// } while (i < 10);

//Break Statement
// for (let i = 0; i < 10; i++) {
//   if (i === 5) {
//     break;
//   }
//   console.log(i);
// }

// for (let i = 0; i < 10; i++) {
//   if (i === 3) {
//     console.log("this is the forth loop but we are not executing all of it , we are continuing");
//     continue;
//   }
//   console.log(i);
// }

// let myName = "Daniel";

// function sayHello() {}

// for (let i = 0; i < 3; i++) {
//   console.log(myName);
//   let favoriteFood = "Burgers";
//   for (let i = 0; i < 2; i++) {
//     console.log(favoriteFood);
//   }
// }
//WONT RUN-> console.log(favoriteFood);

//LET CONST

// let myName = "Daniel";
// console.log(myName);

// myName = "Sam";

// console.log(myName);

// const yourName = "Vladlena";
// console.log(yourName);
// yourName = "Alex";
