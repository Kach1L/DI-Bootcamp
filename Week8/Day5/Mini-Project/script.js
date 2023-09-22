// Retrieving and Declaring All Elements


// All Functions
function displayImageTitle(){
    // let titleDiv = document.querySelector("#imageTitle");
    let titleImage = document.querySelector("#starLogo");
    titleImage.src = "https://www.freepnglogos.com/uploads/star-wars-logo-32.png";
}
displayImageTitle()

let starButton = document.querySelector("#newCharBtn");
starButton.addEventListener("click", getStarInfo);

async function getStarInfo(){
    try{
        let randomNum = Math.floor(Math.random()*83)+1

        let starData = await fetch(`https://www.swapi.tech/api/people/${randomNum}`)
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

            const starButtonContainer = document.querySelector("#buttonDiv");

            let personName = core["result"]["properties"]["name"];
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
                
                starName.value = personName
                starHeight.value = personHeight
                starGender.value = personGender
                starBirthYear.value = personBirthYear
                starHomeWorld.value = homeWorldName                
                
                starContainer.append(`${starName.value} `,`Height: ${starHeight.value} `,`Gender: ${starGender.value} `,`Birth Year: ${starBirthYear.value} `,`Home World: ${starHomeWorld.value}`);

                starButton.addEventListener("click",() => {
                    starContainer.remove()
                    // (starName,starHeight,starGender,starBirthYear,starHomeWorld);
                    getStarInfo();
                })
            }
            
    }
}
    

    



