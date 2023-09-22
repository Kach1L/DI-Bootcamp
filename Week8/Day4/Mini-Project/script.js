// Retrieving and Declaring All Elements


// All Functions
function displayImageTitle(){
    // let titleDiv = document.querySelector("#imageTitle");
    let titleImage = document.querySelector("#starLogo");
    titleImage.src = "https://www.freepnglogos.com/uploads/star-wars-logo-32.png";
    const loading = document.querySelector("i");
    loading.style.opacity = 0;
}
displayImageTitle();

let starButton = document.querySelector("#newCharBtn");
starButton.addEventListener("click",getStarInfo)

async function getStarInfo(){
    const starContainer = document.querySelector("#starWarsData");
    const loading = document.querySelector("i");
    loading.style.color = "white";
    loading.style.fontSize = "150px";
    loading.style.opacity = 1;
    loading.style.marginTop = "120px";
    starContainer.append(loading);

    try{
        const randomNum = Math.floor(Math.random()*83)+1

        const starData = await fetch(`https://www.swapi.tech/api/people/${randomNum}/`);
        // console.log(starData);

        if(!starData.ok){
            throw new Error("Incorrect or Corrupted StarData")
        }else{
            let starInfo = await starData.json()
            // console.log(starInfo);
            displayStarInfo(starInfo)
        }
    } catch(err){
        console.log("In the CATCH ",err);
    }

    async function displayStarInfo(core){
        const starContainer = document.querySelector("#starWarsData");
        const starName = document.createElement("h3");
        const starHeight = document.createElement("h4");
        const starGender = document.createElement("h4");
        const starBirthYear = document.createElement("h4");
        const starHomeWorld = document.createElement("h4");

        // const starButtonContainer = document.querySelector("#buttonDiv");

        const personName = core["result"]["properties"]["name"];
        const personHeight = core["result"]["properties"]["height"];
        const personGender = core["result"]["properties"]["gender"];
        const personBirthYear = core["result"]["properties"]["birth_year"];
        const personHomeWorldPath = core["result"]["properties"]["homeworld"];

        const homeData = await fetch(`${personHomeWorldPath}`)

        if(!homeData.ok){
            throw new Error("Home World LOST!!!");
        }else{
            const homeInfo = await homeData.json();
            // console.log(homeInfo);
            const homeWorldName = homeInfo["result"]["properties"]["name"];
                
            starName.innerText = personName
            starHeight.innerText = personHeight
            starGender.innerText = personGender
            starBirthYear.innerText = personBirthYear
            starHomeWorld.innerText = homeWorldName
            const loading = document.querySelector("i");
            loading.style.display = 'none';              

            starContainer.append(starName, starHeight, starGender, starBirthYear, starHomeWorld);

            starButton.addEventListener("click",() => {
            starName.remove();
            starHeight.remove();
            starGender.remove();
            starBirthYear.remove();
            starHomeWorld.remove();
            loading.style.display = 'block'
            // getStarInfo();
            })
        }
    }
}
    

    



