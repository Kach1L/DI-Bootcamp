// when I submit the form, I want to retrieve whatever is in the input tag
const gifForm = document.querySelector("#gifForm");
gifForm.addEventListener("submit", getInput);

async function getInput(event) {
    event.preventDefault(); //mandatory
    //event.target is the whole form
    // const inputValue = event.target.category.value;
    // console.log(inputValue);
    const dataForm = new FormData(event.target);
    const dataValue = Object.fromEntries(dataForm); //{category: 'a'}
    await getGif(dataValue["category"]); //2sec
    await getJoke(dataValue["category"]); //3sec
}

async function getJoke (category) {
    try {
        const url = `https://api.chucknorris.io/jokes/search?query=${category}`
        const resp = await fetch(url);
        if (!resp.ok) {
            throw new Error("error fetching Joke")
        } else {
            const joke = await resp.json();
            console.log(joke["result"][0].value);
        }
    } catch (error) {
        console.log("OOPS ", error);
    }
}

async function getGif (category) {
    try {
        const url = `https://api.giphy.com/v1/gifs/random?tag=${category}&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`
        const resp = await fetch(url);
        if (!resp.ok) {
            throw new Error("error fetching gif")
        } else {
            const gif = await resp.json();
            const gifURL = gif["data"]["images"]["original"]["url"];
            displayGif(gifURL)
        }
    } catch (error) {
        console.log("OOPS ", error);
    }
}


function displayGif (url) {
    const section = document.querySelector("#allGifs");
    const imgGif = document.createElement("img");
    imgGif.src = url;
    section.appendChild(imgGif)
}





// const testInput = document.querySelector("#testInput");
// testInput.addEventListener("input", (event) => {
//     console.log(event.target.value)
// })

// testInput.addEventListener("keydown", (event) => {
//     console.log(event.target.value)
// })