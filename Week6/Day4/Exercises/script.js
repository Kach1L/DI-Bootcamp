// // Exercises1 #1
const people = ["Greg", "Mary", "Devon", "James"];
// console.log(people);
// people.splice(0,1);
// console.log(people);
// // #2
// people.splice(-1,1,'Jason');
// console.log(people);
// // #3
// people.push('Kachi');
// console.log(people);
// // #4
// maryIndex = people.indexOf('Mary');
// console.log(maryIndex);
// // #5
// peopleCopy = people.slice(1,3);
// console.log(peopleCopy);
// // #6
// fooIndex = people.indexOf('Foo')
// console.log(fooIndex);
// // #7
// last = people.slice(-1)
// console.log(last);


// Part2 #1
// for (let i of people){
//     console.log(i)
// }
// #2
// for(let i of people){
//     if(i !== 'Devon'){
//         console.log(i)
//     }
//     else{
//         break
//     }
// }

// Exercises2 #1
// const colors = ['red','blue','black','yellow','white']
// const suffixes = ['st','nd','rd','th','th']

// #2
// let i=0
// while (i<5){
//     console.log('My #' + i + ' choice is ' + colors[i]);
//     i++;
// }

// #3
// let x=0
// while (x<5){
//     console.log('My '+ x + suffixes[x] + ' choice.');
//     x++;
// }


// Exercises3 #1
// userNumber = prompt('Give a number');
// numType = typeof userNumber;
// console.log(numType);

// #2
// i=0
// while(i<10){
//     userNumber = prompt('Give a number');
//     console.log(userNumber)
//     i++
// }


// Exercises4 #1
// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }
// #2
// console.log(building.numberOfFloors);

// #3
// console.log(building.numberOfAptByFloor.firstFloor);
// console.log(building.numberOfAptByFloor.thirdFloor);

// #4
// console.log(building.nameOfTenants[1])
// console.log(building.numberOfRoomsAndRent.dan[0])
// sarahSum = building.numberOfRoomsAndRent.sarah[1]
// davidSum = building.numberOfRoomsAndRent.david[1]
// danSum = building.numberOfRoomsAndRent.dan[1]

// console.log(sarahSum)
// console.log(davidSum)
// if (sarahSum < danSum && davidSum < danSum){
//     sarahSum += 1200
//     davidSum += 1200
// }
// else{
//     console.log(false)
// }
// console.log(sarahSum)
// console.log(davidSum)


// Exercise 5 #1
const family = {
    father: "John",
    mother: "Jane",
    children: ["Alice", "Bob", "Eve"],
};
  
// // #2
// // Console.log the keys of the object
// for (let key in family) {
//     console.log(key);
// }

// // #3
// // Console.log the values of the object
// for (let key in family) {
// console.log(family[key]);
// }


// // Exercise 6 #1
// const details = {
//     my: "name",
//     is: "Rudolf",
//     the: "raindeer",
// };
  
// let result = "";
 
// // #2
// // Concatenate the values using a for-in loop
// for (let key in details) {
//     result += details[key] + " ";
// }

// // #3
// console.log(result.trim()); // Output: "my name is Rudolf the raindeer"


// // Exercise 7 #1
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
const sortedLetters = names.map(name => name[0]).sort().join("");

// // #2
// console.log(sortedLetters); // Output: "ABJKPS"

  




// DAILY CHALLENGE1
// #1
const sentence = "The movie is not that bad, I like it";

// #2
// const wordNot = sentence.indexOf("not");
// const wordBad = sentence.indexOf("bad");

// #3
// if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
//   const newSentence = sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
//   console.log(newSentence);
// } else {
//   console.log(sentence);
// }





// DAILY CHALLENGE2
// #1
// star = '*'
// star2 = '*'
// console.log(star)
// for(i=0;i<5;i++){
//     star+='*'
//     console.log(star)
//     }
// console.log('\t   ' + star2)
// for(k=0;k<5;k++){
//         star2+='*'
//         console.log('\t   ' + star2)
// }

// Extra with WHILE
// star = '*'
// star2 = '*'
// console.log('\t   \t     ' + star)
// i=0
// while(i<5){
//     star+='*'
//     console.log('\t   \t     ' + star)
//     i++
// }
// console.log('\t   \t     \t   ' + star2)
// j=0
// while(j<5){
//     star2+='*'
//     console.log('\t   \t     \t   ' + star2)
//     j++
// }
