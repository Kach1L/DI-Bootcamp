// Ex 1
// function compareToTen(num) {
//     return new Promise((resolve,reject) => {
//         if(num<=10){
//             console.log("resolve")
//             resolve("less than 10 and not equal")
//         }
//         else{
//             console.log("reject")
//             reject("error: more than 10")
//         }
//     })
// }
//In the example, the promise should reject
// compareToTen(15)
//   .then((result) => console.log(result))
//   .catch((error) => console.log(error))

//In the example, the promise should resolve
// compareToTen(8)
//   .then((result) => console.log(result))
//   .catch((error) => console.log(error))




    // new Promise((resolve,reject) => {
    //     if(num<=10){
    //         console.log("resolve")
    //         resolve("less than 10 and not equal")
    //     }
    //     else{
    //         console.log("reject")
    //         reject("error: more than 10")
    //     }
    // })

// // In the example, the promise should reject
// compareToTen(15)
//   .then((result) => console.log(result))
//   .catch((error) => console.log(error))



// Ex 2
//   const mySecondPromise = new Promise ((resolve, reject) => {
// 	console.log("Self resolver")

// 	setTimeout(() => {
// 		if (true) {
// 			console.log("resolve")
// 			resolve("success")
// 		} else {
// 			console.log("reject")
// 			reject("failure")
// 		}
// 	}, 4000)
// })

// mySecondPromise.then((res) => console.log(res));
// mySecondPromise.catch((error) => console.log(error));




// Ex 3
// const resolvedPromise = Promise.resolve(3);

//   resolvedPromise
//     .then((result) => console.log("Resolved: ", result))
//     .catch((error) => console.log("Rejected: ", error));


// const rejectedPromise = Promise.reject("Boo!")

//     rejectedPromise
//     .then((result) => console.log("Resolved: ", result))
//     .catch((error) => console.log("Rejected: ", error));

