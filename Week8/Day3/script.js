const btn = document.querySelector("#btn");
btn.addEventListener("click", getData)

function getData () {
    fetch("https://api.chucknorris.io/jokes/random")
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
        const liElement = document.createElement("li");
        const text = document.createTextNode(`The random joke is - ${data["value"]}`);
        liElement.appendChild(text);
        ulElement.appendChild(liElement)
        
    })
    .catch((error) => console.log("IN THE CATCH", error))
}







