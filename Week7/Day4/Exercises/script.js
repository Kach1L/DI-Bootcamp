// Ex 1
const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

// colors.forEach((color, index) => {
//   console.log(`${index + 1}# choice is ${color}.`);
// });

// if (colors.includes("Violet")) {
//   console.log("Yeah");
// } else {
//   console.log("No...");
// }



// Ex 2
// const ordinal = ["th", "st", "nd", "rd"];

// colors.forEach((color, index) => {
//   const ordinalIndex = (index < 3) ? index + 1 : 0;
//   const ordinalSuffix = ordinal[ordinalIndex];
//   console.log(`${index + 1}${ordinalSuffix} choice is ${color}.`);
// });



// Ex 3 #1
// const fruits = ["apple", "orange"];
// const vegetables = ["carrot", "potato"];

// const result = ['bread', ...vegetables, 'chicken', ...fruits];
// console.log(result); // Output: ["bread", "carrot", "potato", "chicken", "apple", "orange"]

// // #2
// const country = "USA";
// console.log([...country]); // Output: ["U", "S", "A"]

// // Bonus
// let newArray = [...[,,]];
// console.log(newArray); // Output: [undefined, undefined]



// Ex 4
// const users = [
//     { firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
//     // ... other users
//   ];
  
//   const welcomeStudents = users.map(user => `Hello ${user.firstName}`);
//   const fullStackResidents = users.filter(user => user.role === 'Full Stack Resident');
//   const fullStackResidentsLastNames = fullStackResidents.map(user => user.lastName);
  
//   console.log(welcomeStudents);
//   console.log(fullStackResidents);
//   console.log(fullStackResidentsLastNames);



// Ex 5
// const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

// const combinedString = epic.reduce((acc, word) => acc + " " + word);
// console.log(combinedString); // Output: "a long time ago in a galaxy far far away"



// Ex 6
const students = [
    {name: "Ray", course: "Computer Science", isPassed: true},
    // ... other students
  ];
  
  const passedStudents = students.filter(student => student.isPassed);
  passedStudents.forEach(student => {
    console.log(`Good job ${student.name}, you passed the course in ${student.course}.`);
  });
  

