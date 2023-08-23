// const gameInfo = [
//     {
//       username: "john",
//       team: "red",
//       score: 5,
//       items: ["ball", "book", "pen"]
//     },
//     {
//       username: "becky",
//       team: "blue",
//       score: 10,
//       items: ["tape", "backpack", "pen"]
//     },
//     {
//       username: "susy",
//       team: "red",
//       score: 55,
//       items: ["ball", "eraser", "pen"]
//     },
//     {
//       username: "tyson",
//       team: "green",
//       score: 1,
//       items: ["book", "pen"]
//     },
// ];

// #1
// const username = [];

// gameInfo.forEach((info,i) =>{
//     info["username"] += '!'
//     username.push(info["username"])
// });

// console.log(username);



// #2
// const winners = []

// gameInfo.forEach((info) =>{
//     if (info["score"] > 5){
//         winners.push(info["username"])
//     }
//     else{
//         console.log(`${info["username"]} score is smaller than 5`);
//     }
// });

// console.log(winners);



// #3
// totalScore = 0

// gameInfo.forEach((info) =>{
//     totalScore += info["score"]
// });

// console.log('The total score is '+ totalScore);





// Daily Challenge: Car Inventory
// Part I
// const inventory = [
//     { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
//     { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
//     { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
//     { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
//     { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
//   ];
  
//   function getCarHonda(carInventory) {
//     const hondaCar = carInventory.find(car => car.car_make === "Honda");
//     if (hondaCar) {
//       return `This is a ${hondaCar.car_make} ${hondaCar.car_model} from ${hondaCar.car_year}.`;
//     } else {
//       return "No Honda car found in inventory.";
//     }
//   }
  
//   console.log(getCarHonda(inventory)); // Output: "This is a Honda Accord from 1983."



// Part II
// function sortCarInventoryByYear(carInventory) {
//     return carInventory.slice().sort((a, b) => a.car_year - b.car_year);
//   }
  
//   const sortedInventory = sortCarInventoryByYear(inventory);
//   console.log(sortedInventory); // Output: The sorted inventory as described in the instructions.
  




  