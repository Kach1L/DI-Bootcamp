// synchronous
console.log("1");
console.log("2");
console.log("3");

// synchronous
function funcOne (name, callback){ //2
    console.log("In the first function");
    callback(name) // funcTwo("John") //3
    console.log("hello") //5
}

function funcTwo (name){ //4
    console.log("In the callback function"); 
    console.log(name.toUpperCase()); //"JOHN"
}

funcOne("John", funcTwo) //1
//passing to the funcOne the reference to the funcTwo function



// synchronous
function task(message) { //3
    // emulate time consuming task
    let n = 10000000000;
    while (n > 0){
        n--;
    }
    console.log(message);
}

console.log('Start script...'); //1
task('Download a file.'); //2
console.log('Done!');

let btn = document.querySelector("button");
btn.addEventListener("click", () => console.log("clicked"))

// asynchronous
// setTimeout() is an asynchronous function, 
// meaning that the timer function will not pause 
// execution of other functions in the functions stack.
console.log("1"); //1
console.log("2"); //2

setTimeout(function (){ //3
    console.log("callback function") //6
},2000)

console.log("3");//4
console.log("4");//5


setTimeout(
    function(){console.log("this is the first message")}, 
1000);

setTimeout(
    function(){console.log("this is the second message")}, 
1000);

setTimeout(
    function(){console.log("this is the third message")}, 
1000);

