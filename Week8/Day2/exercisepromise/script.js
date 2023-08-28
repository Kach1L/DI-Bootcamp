function check(input) {
    const myPromise = new Promise((resolve, reject) => {
        setTimeout (() => { 
            if (typeof input === 'string') {
                resolve(input.toUpperCase())
            } else {
                reject("Not a string")
            }
        }, 3000)
    })
    return myPromise;
}

check("abc")
.then((result) => console.log((result+" ").repeat(2).trim()))
.catch((error) => console.log("IN THE CATCH, THE ERROR IS ", error))
.finally(() => console.log("congratulations"))

check(123)
.then((result) => console.log(result.repeat(2)))
.catch((error) => console.log("IN THE CATCH, THE ERROR IS ", error))
.finally(() => console.log("congratulations"))