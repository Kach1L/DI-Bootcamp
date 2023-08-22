// Ex 1
// #1
// function funcOne() {
//     let a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }

// // #1.1 - run in the console:
// funcOne() 
// I think alert will give 3.

// #1.2 What will happen if the variable is declared 
// with const instead of let ?
// There will be an error because with const the variable can't be redeclared


//#2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// // #2.1 - run in the console:
// funcThree()
// funcTwo()
// funcThree()
// Firstly a will = 0, then a will be changed to 5 then a will = 5

// #2.2 What will happen if the variable is declared 
// with const instead of let ?
// There will be an error because with const the variable can't be redeclared


// //#3
// function funcFour() {
//     window.a = "hello";
// }


// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// // #3.1 - run in the console:
// funcFour()
// funcFive()
// It will give hello

// //#4
// let a = 1;
// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);
// }


// // #4.1 - run in the console:
// funcSix()
// The function changes a from 1 to "test" and alerts it
// #4.2 What will happen if the variable is declared 
// with const instead of let ?
// There will be an error because with const the variable can't be redeclared


// //#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// #5.1 - run the code in the console
// The if statement changes a from 2 to 5 and alerts it in the if statement but outside the condition the alert prints its prior value, 2
// #5.2 What will happen if the variable is declared 
// with const instead of let ? 
// Nothing because the variables are declared in 2 different scopes



// Ex 2
// winBattle = () =>{return true};
// let experiencePoints = 0;

// if (winBattle() == true){
//     let experiencePoints = 10;
//     console.log(experiencePoints);
// }



// Ex 3
// isString = (value) =>{
//     if (typeof value == "string") {
//         return true;
//     }
//     else{
//         return false
//     }
// }

// console.log(isString('hello')); 
// //true
// console.log(isString([1, 2, 4, 0]));
// //false



// Ex 4
// oneLineSum = (a,b) => a + b;
// sum = oneLineSum(7,7)

// console.log(sum);



// Ex 5
// function kgToGr1(k){
//     res = k/1000;
//     return res;
// }
// console.log(kgToGr1(5000));

// const kgToGr2 = function (k) {return k/1000};
// console.log(kgToGr2(5000));

// // Difference: Expression is shorter and simpler than a declaration
// const kgToGr3 = (k) => k/1000;
// console.log(kgToGr3(5000));



// Ex 6
// (function(numberOfChildren, partnerName, geographicLocation, jobTitle) {
//     const fortune = `You will be a ${jobTitle} in ${geographicLocation}, and married to ${partnerName} with ${numberOfChildren} kids.`;
//     document.write(fortune);
// });
// (2, 'Emma', 'New York', 'Software Engineer');



// Ex 7
// (function(userName) {
//     const userProfileDiv = document.getElementById('userProfile');
//     const userProfileHTML = `
//         <img src="profile_picture.jpg" alt="Profile Picture">
//         <p>Welcome, ${userName}!</p>
//     `;
//     userProfileDiv.innerHTML = userProfileHTML;
// })('John');



// Ex 8
// function makeJuice(size) {
//     const ingredients = [];

//     function addIngredients(ingredient1, ingredient2, ingredient3) {
//         ingredients.push(ingredient1, ingredient2, ingredient3);
//     }

//     addIngredients('apple', 'orange', 'banana');
//     addIngredients('strawberry', 'kiwi', 'mango');

//     function displayJuice() {
//         const juiceInfo = `The client wants a ${size} juice, containing ${ingredients.join(', ')}.`;
//         document.write(juiceInfo);
//     }

//     displayJuice();
// }

// makeJuice('large');








