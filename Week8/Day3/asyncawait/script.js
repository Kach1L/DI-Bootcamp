// function check () {
//     return new Promise ((resolve, reject) => {
//         if (condition) {
//             resolve()
//         } else {
//             reject()
//         }
//     })
// }

// function returns a promise
async function check () {
    return "hello"
}

console.log(check())

const grade = 89
// //returns a promise
async function checkTwo () {
    if (grade > 65) {
        return {gift:"computer"}; // same as resolve
    } else {
        throw new Error ("not good grade");
    }
}

checkTwo()
.then((result) => console.log("I got a ", result["gift"]))
.catch((error) => console.log("in the catch", error))

//async await
function js () {
    return new Promise ((resolve, reject) => {
        setTimeout(() => {
            console.log("in process of js");
            resolve("heyyy")
        }, 4000)
    })
}

function react () {
    return new Promise ((resolve, reject) => {
        setTimeout(() => {
            console.log("in process of react");
            resolve("byeee")
        }, 1000)
    })
}

//outside the function is asynchronous
//inside the function is it synchronous
async function learning () {
    //await wait for the promise to be settled
    //retrieve the result of the promise
    //AWAIT IS ONLY USED TO WAIT FOR PROMISES
    try  {
        const resultOne = await js();
        console.log(resultOne); //heyyy
        console.log("I learned Javascript");
        const resultTwo = await react()
        console.log(resultTwo); //byeee
        console.log("I learned React");
    } catch (error) {
        console.log("IN THE CATCH");
    }
}

learning()

for (let i=0; i< 200; i++) {
    console.log("hello");
}


// js()
// .then(() => react())