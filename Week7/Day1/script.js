// function greet(username,age){
//     console.log(`Welcome to the page ${username}, you're ${age} years old`);
// }

// greet('Daniel',23)
// greet('Kachi',16)


// function ages(myAge){
//     console.log(`My mums age is ${myAge*2} and my dads is ${myAge*2*1.2}`)
// }
// ages(15)

// function calculate(x,y){
//     let mySum = x + y
//     return mySum;
// }
// let sum = calculate(1,2)
// console.log(sum)

function exeptions(){
    try {
      console.log('h');
    } catch(e){
      console.log(e.name);
      console.log(e.message);
      console.log(e.stack);
    } finally {
      console.log("I will run in any case");
    }
}

exeptions();
