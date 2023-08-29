const userInput = document.querySelector("#searchBox");
const userButton = document.querySelector("#btn1");
const deleteButton = document.querySelector("#btn2");
const userImage = document.querySelector("img");

async function retrieveSearchData(search) {
    // e.preventDefault()
    const randomData = await fetch(`https://api.giphy.com/v1/gifs/random?q=${search}&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`);
    try{
        if (!randomData.ok){
        throw new Error("gifData couldn't be retrieved");
    } else{
        const randomInfo = await randomData.json()
        console.log(randomInfo);
        source = randomInfo["data"]["images"]["downsized"]["url"]
        userImage.src = source
    }  } catch(err){
        console.error("IN THE CATCH", err);
    }

    deleteButton.textContent = "Delete";
    deleteButton.addEventListener("click", () => {
        userImage.remove();
    });
}
retrieveSearchData(userInput.value)