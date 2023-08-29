const arrOne = ["blue", "red", ["yellow", "green"]]
const arrTwo = [...arrOne] //spread operator
// shallow copy
// superficial
// not going to copy the inner array or object

arrOne[0] = "black"

console.log(arrOne);
// (3) ['black', 'red', Array(2)]
console.log(arrTwo);
// (3) ['blue', 'red', Array(2)]

arrOne[2][0]= "pink"

console.log(arrOne);
// (3)['black', 'red', Array(2)]
// 0: "black"
// 1: "red"
// 2: (2)['pink', 'green']

console.log(arrTwo);
// (3)['blue', 'red', Array(2)]
// 0: "blue"
// 1: "red"
// 2: (2)['pink', 'green']

// deep copy
// JSON.stringify : takes a javascript object and converts it
// into a json string
// JSON.parse : take a json string and converts it into a javascript object
const arrThree = JSON.parse(JSON.stringify(arrOne))
