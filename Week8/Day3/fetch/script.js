// syntax to make a request
// by default is a GET request

// fetch method returns a Promise
// The promise resolves to the Response object 
// representing the response to your request.

// console.log(fetch("https://jsonplaceholder.typicode.com/users"))

fetch("https://jsonplaceholder.typicode.com/users")
.then((response) => {
    if (!response.ok) {
        throw new Error("problem with fetch")
    } else {
        return response.json()
        //method retrieve the data and parses it
    }
})
.then((data) => console.log(data))
.catch((error) => console.log("IN THE CATCH", error))

//WITH BUTTON
const btn = document.querySelector("#btn");
btn.addEventListener("click", getData)

function getData () {
    fetch("https://jsonplaceholder.typicode.com/users")
    .then((response) => {
        if (!response.ok) {
            throw new Error("problem with fetch")
        } else {
            return response.json()
            //method retrieve the data and parses it
        }
    })
    .then((data) => {
        const ulElement = document.querySelector("#results")
        data.forEach(user => {
            const liElement = document.createElement("li");
            const text = document.createTextNode(`${user["name"]} - ${user["email"]}`);
            liElement.appendChild(text);
            ulElement.appendChild(liElement)
        });
    })
    .catch((error) => console.log("IN THE CATCH", error))
}

// when you use the fetch method
// you receive a Response object
// the Response object contains info about the request
// and the response
// but it doesnt contain the data

// EXERCISE RandomJokes
function getJokes () {
    fetch("https://api.chucknorris.io/jokes/random")
    .then((response) => {
        if (!response.ok) {
            throw new Error("problem with fetch")
        } else {
            return response.json();
            //method retrieve the data and parses it
            //returning a promise with the data as the result
        }
    })
    .then((data) => {
        const ulElement = document.querySelector("#results")
        if (ulElement.children[0]) {
            ulElement.children[0].remove();
        }
        const liElement = document.createElement("li");
        const text = document.createTextNode(`${data["value"]}`);
        liElement.appendChild(text);
        ulElement.appendChild(liElement)
    })
    .catch((error) => console.log("IN THE CATCH", error))
}

getJokes()

// get other jokes
async function getOtherJokes () {
    try {
        const response = await fetch("https://api.chucknorris.io/jokes/random")
        if (!response.ok) {
            throw new Error("problem with fetch")
        } else {
            const data = await response.json();
            displayData(data)
        }
    } catch (err) {
        console.log("IN THE CATCH ", err);
    }
}


function displayData(data) {
    const ulElement = document.querySelector("#results")
    const liElement = document.createElement("li");
    const text = document.createTextNode(`${data["value"]}`);
    liElement.appendChild(text);
    ulElement.appendChild(liElement)
}


getOtherJokes()

for (let i=0; i < 5000; i++) {
    console.log("hello");
}



