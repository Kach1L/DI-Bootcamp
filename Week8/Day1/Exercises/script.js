// Ex 1
// const person = {
//     name: 'John Doe',
//     age: 25,
//     location: {
//         country: 'Canada',
//         city: 'Vancouver',
//         coordinates: [49.2827, -123.1207]
//     }
// }

// const {name, location: {country, city, coordinates: [lat, lng]}} = person;

// console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);
// The output will be all the values of the person object.




// Ex 2
// function displayStudentInfo(objUser){
//     //destructuring
//     const {first:f, last:l} = objUser
//     console.log(`Your full name is ${f} ${l}.`);
//     return `Your full name is ${f} ${l}.`
// }

// displayStudentInfo({first: 'Elie', last:'Schoppik'});




// Ex 3
// const users = {user1: 18273, user2: 92833, user3: 90315};

// function turnToArray(){
//     // Convert the object to an array of arrays
//     const usersArray = Object.entries(users);

//     console.log(usersArray); // Output: [ [ 'user1', 18273 ], [ 'user2', 92833 ], [ 'user3', 90315 ] ]

//     // Multiply the user's ID by 2
//     const multipliedUsersArray = usersArray.map(([user, id]) => [user, id * 2]);

//     console.log(multipliedUsersArray); // Output: [ [ 'user1', 36546 ], [ 'user2', 185666 ], [ 'user3', 180630 ] ]
// }
// turnToArray()




// Ex 4
// class Person {
//     constructor(name) {
//       this.name = name;
//     }
//   }
  
//   const member = new Person('John');
//   console.log(typeof member);




// Ex 5
// class Dog {
//     constructor(name) {
//       this.name = name;
//     }
//   };

// class Labrador extends Dog {
//     constructor(name, size) {
//       super(name);
//       this.size = size;
//     }
//   };




// Ex 6
// a = [2] === [2] 
// b = {} == {}
// console.log(a, b)
// Both are false


const object1 = { number: 5 }; 
const object2 = object1; 
const object3 = object2; 
const object4 = { number: 5};

object1.number = 4;
console.log(object2.number)
console.log(object3.number)
console.log(object4.number)


// class Animal {
//     constructor(name, type, color) {
//       this.name = name;
//       this.type = type;
//       this.color = color;
//     }
//   }
  
//   class Mammal extends Animal {
//     sound(sound) {
//       return `Moooo I'm a ${this.type}, named ${this.name} and I'm ${this.color}. ${sound}`;
//     }
//   }
  
//   const farmerCow = new Mammal("Lily", "cow", "brown and white");
//   const cowSound = farmerCow.sound("Moooo");
//   console.log(cowSound); // Output: Moooo I'm a cow, named Lily and I'm brown and white. Moooo
  