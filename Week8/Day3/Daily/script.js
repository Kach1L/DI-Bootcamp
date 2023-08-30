const userInput = document.querySelector("#searchBox");
const userImage = document.querySelector("img");
const userButton = document.querySelector("#btn1");
const deleteButton = document.querySelector("#btn2");
const gifForm = document.querySelector("#gifForm");

// gifForm.addEventListener("submit",retrieveSearchData);

async function retrieveSearchData(search) {
    const randomData = await fetch(`https://api.giphy.com/v1/gifs/random?q=${search}&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`);
    try{
        if (!randomData.ok){
        throw new Error("gifData couldn't be retrieved");
    } else{
        const randomInfo = await randomData.json()
        console.log(randomInfo);
        const source = randomInfo["data"]["images"]["original"]["url"]
        userImage.src = source;
    }  } catch(err){
        console.error("IN THE CATCH", err);
    }

    deleteButton.addEventListener("click", () => {
        userImage.remove();
    });
}
retrieveSearchData(userInput.value);