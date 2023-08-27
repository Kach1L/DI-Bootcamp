// Advanced object methods
const object1 = {
  a: "somestring",
  b: 42,
  c: false,
};

//Get keys
// console.log(Object.keys(object1));

// //Get values
// console.log(Object.values(object1));

//Get key value pairs
// const newArr = Object.entries(object1);
// console.log(newArr);

// //Array to Object (accepts arr key value pairs)
// const newerArr = [
//   ["name", "daniel"],
//   ["age", "almost30help"],
// ];
// console.log(Object.fromEntries(newerArr));

//Exercise 1
// let myObj = {
//   name: "John",
//   lastName: "Doe",
//   age: 25,
//   friends: ["Mark", "Lucie", "Ana"],
// };

// const newArr = Object.entries(myObj);

// newArr.forEach((element, index) => {
//   const pos = index + 1;
//   console.log(`The #${pos} key is ${element[0]}. The #${pos} value is ${element[1]} `);
// });

//Object Destructuring
// const address = {
//   street: "Evergreen Terrace",
//   number: "742",
//   city: "Springfield",
//   state: "NT",
//   zip: "49007",
// };

//Getting values regular way:

// const street = address.street;
// console.log(street);

//Destructuring ,custom variable names;
// const { street: s, city: c } = address;

// console.log(s);
// console.log(c);

//Destructing values saved in key names
// const { street, city } = address;

// console.log(street);
// console.log(city);

//Nested OBJ destructuring

// const student = {
//   name: "John Doe",
//   age: 16,
//   scores: {
//     maths: 74,
//     english: 63,
//   },
// };

// const {
//   name,
//   scores: { maths, science = 56 },
// } = student;

// console.log(`${name} scored ${maths} in maths and ${science} in science`);

//Destructuring in function parameters

// const student = {
//   name: "John Doe",
//   age: 16,
//   scores: {
//     maths: ["i", "a", "s"],
//     english: 63,
//     science: 85,
//   },
// };

// function displaySummary({ name, scores: { maths = 0, english = 0, science = 0 } }) {
//   console.log("Hello, " + name);
//   console.log("Your Maths score is " + maths);
//   console.log("Your English score is " + english);
//   console.log("Your Science score is " + science);
// }

// displaySummary(student);
// console.log(student);

//SPREAD OPERATOR
// let obj = { foo: 1, bar: 2 };
// let newObj = { ...obj, baz: 3 };
// console.log(newObj);

// let obj = { foo: 1, bar: 2, baz: 3 };
// let newObj = { ...obj, foo: true };
// console.log(newObj);

// let obj = { foo: 1, bar: 2, baz: 3 };
// let newObj = { foo: true, ...obj };
// console.log(newObj);

//Shallow Copy
// let myCar = {
//   color: "blue",
//   details: {
//     plateNumber: 123,
//     name: "Ford",
//   },
// };

// let myNewCar = { ...myCar };
// console.log(myNewCar === myCar);

// myCar.color = "red";
// console.log(myNewCar);

//Classes (not css classes)

// class Rectangle {
//   constructor(height, width) {
//     this.height = height;
//     this.width = width;
//   }
//   calcArea() {
//     return this.height * this.width;
//   }
// }

// const square = new Rectangle(10, 10);
// console.log(square.calcArea());

// const biggerSquare = new Rectangle(20, 20);
// console.log(biggerSquare.calcArea());

//Exercise
// class Rabbit {
//   constructor(type) {
//     this.type = type;
//   }
//   speak(line) {
//     console.log(`The ${this.type} rabbit says '${line}'`);
//   }
// }

// let killerRabbit = new Rabbit("killer");
// let blackRabbit = new Rabbit("black");

// killerRabbit.speak("death");
// blackRabbit.speak("Hello");

//Getters & Setters

// class Rectangle {
//   constructor(height, width) {
//     this.height = height;
//     this.width = width;
//   }
//   get area() {
//     return this.height * this.width;
//   }

//   set area(factor) {
//     this.width = this.height * factor;
//   }
// }

// const square = new Rectangle(10, 10);
// console.log(square.area);
// square.area = 2;
// console.log(square.area);

//Extending classes

// class Animal {
//   constructor(name) {
//     this.name = name;
//   }
//   speak() {
//     console.log(`${this.name} makes a noise.`);
//   }
// }

// class Dog extends Animal {
//   constructor(name, noise) {
//     super(name);
//     this.noise = noise;
//   }
//   speak() {
//     console.log(`${this.name} barks.it says ${this.noise}`);
//   }
// }

// let newDog = new Dog("Mitzie", "Wouaf");

// newDog.speak();

// class Golden extends Dog {
//   constructor(noise, color) {
//     super(noise);
//     this.color = color;
//   }
//   speak() {
//     console.log(`${this.name} barks.it says ${this.noise}. its color is ${this.color}`);
//   }
// }

// const goldenDoggo = new Golden("bob", "woof", "golden");

// goldenDoggo.speak();
// let date = document.getElementById("datetime");
// date.addEventListener("change", function (event) {
//   //   console.log(event.target.value);
//   let date = new Date(event.target.value);
//   console.log(date.getDay());
// });

// let currentDate = new Date();
// console.log(currentDate.getDay());
// let dayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
// console.log(dayNames[currentDate.getDay()]);
// console.log(currentDate.getMonth() + 1);
// console.log(currentDate.getDate());
// console.log("getFullYear", currentDate.getFullYear());
// console.log("getHours", currentDate.getHours());
// console.log("getMinutes", currentDate.getMinutes());
// console.log("getSeconds", currentDate.getSeconds());
// console.log("getMilliseconds", currentDate.getMilliseconds());

// console.log("getTime", currentDate.getTime());
// let today = new Date();
// let anotherDay = new Date(2021, 1, 19, 11, 55);

// let diff = anotherDay - today;
// console.log(diff);
// let days = diff / (1000 * 60 * 60 * 24);
// console.log(Math.floor(days));

// let currentDate = new Date();
// console.log(currentDate.getMonth() + 1);
