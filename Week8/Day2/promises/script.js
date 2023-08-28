const grade = 80;

const myFirstPromise = new Promise((resolve, reject) => {  
    if (grade > 75) {
        resolve({gift: "computer"});
        //pass into the resolve the result of the promise
        //something that I will get if the promise is successful
    } else {
        reject("Not enough grade");
        //pass into the reject the reason of the failed promise
        //something that I will get if the promise is rejected
    }
});

console.log(myFirstPromise);


const mySecondPromise = new Promise ((resolve, reject) => {
	console.log("start")
	const grade = 60;

	setTimeout(() => {
		if (grade >= 70) {
			// console.log("resolve")
			resolve({gift:"computer"})
		} else {
			// console.log("reject")
			reject("Low grades")
		}
	}, 3000)
})

// then method is to wait for the promise to come
// back resolved and retrieve the data 
// returned by the promise

//consume the promise
// at the end of the 3 second
// State : resolved
// Result : {gift:"computer"}

// State : rejected
// Result : "Low grades"

mySecondPromise
.then((result) => console.log("I GOT A GIFT", result))
.catch((error) => console.log("IN THE CATCH, the error is ", error))


// loop will run while we wait 3 seconds
// Promises are the foundation of asynchronous programming 
// in modern JavaScript. A promise is an object 
// returned by an asynchronous function, 
// which represents the current state of the operation
for (let i = 0; i < 100 ; i++) {
    console.log("hello");
}

mySecondPromise
    .then((giftFromMum) => {
        console.log("in the first then", giftFromMum);
        // console.log(hello);
        // throw new Error ("errorrrrrrr")
        return "my mum is great";
    })
    .then((result) => {
        console.log("in the 2nd then", result)
    })
    .catch((error) => console.log("IN THE CATCH, the error is ", error))

// //--> doanything


// // getLocation (its a promise)
// // .then ((city) => get the weather (a promise) and return it)
// // .then((weather) => display it)
