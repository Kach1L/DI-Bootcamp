function first () {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("abc")
        }, 2000)
    })
}

function second () {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("123")
        }, 3000)
    })
}

// async function check () {
//     const startTime = performance.now()
//     await first();
//     await second();
//     const endTime = performance.now()
//     console.log(`Call to doSomething took ${endTime - startTime} milliseconds`)
// }

// check()

async function check () {
    const startTime = performance.now()
    console.log(startTime); //timestamp
    const results = await Promise.all([first(), second()])
    console.log(results); //['abc', '123']
    const endTime = performance.now()
    console.log(`Call to doSomething took ${endTime - startTime} milliseconds`)
}

check()