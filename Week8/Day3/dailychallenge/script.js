const  makeAllCaps = (words)  => {
    return new Promise ((resolve, reject) => {
        if (words.every((element) => typeof element === "string")) {
            const uppercasedArray = words.map((word) => word.toUpperCase())
            resolve(uppercasedArray)
        } else {
            reject("not all strings")
        }
    })
}

const sortWords = (upperWords) => {
    return new Promise((resolve, reject) => {
        if (upperWords.length > 4) {
            // const newArr = upperWords.toSorted();
            // toSorted method create a new array sorted
            const newArr = [...upperWords].sort();
            resolve(newArr)
        } else {
            reject("array not long enough")
        }
    })
}


// console.log(sortWords(['BLUE', 'RED', 'YELLOW', 'PINK', 'BLACK']));

makeAllCaps(["blue", "red", "yellow"])
.then((upperArr) => sortWords(upperArr))
.then((sortedArr) => console.log(sortedArr)) //an array that is uppercased and sorted
.catch((error) => console.log("IN THE CATCH"))


