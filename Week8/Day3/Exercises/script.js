// Ex 1
// async function retrieveData() {
//     const gifData = await fetch("https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My")
//     if (!gifData.ok){
//         throw new Error("gifData couldn't be retrieved");
//     } else{
//         const gifs = await gifData.json()
//         console.log(gifs);    
//     }  
// }
// retrieveData()




// Ex 2
// async function retrieveSunData() {
//         const filteredGifData = await fetch("https://api.giphy.com/v1/gifs/search?offset=2&limit=10&q=sun&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My");
//         if (!filteredGifData.ok){
//             throw new Error("gifData couldn't be retrieved");
//         } else{
//             const filteredGifs = await filteredGifData.json()
//             console.log(filteredGifs);    
//         }  
//     }
// retrieveSunData()





// Ex 3
// async function retrieveStarWars() {
//     try {
//         const starData = await fetch("https://www.swapi.tech/api/starships/9/");
//         if (!starData.ok){
//             throw new Error("Corrupted Star Wars Data!!!");
//         } else{
//             // console.log(starData.json());
//             const starInfo = await starData.json();
//             console.log(starInfo);
//         }
//     } catch (err) {
//         console.log("in the catch", err);
//     }
   
// }
// retrieveStarWars()




// Ex 4
// function resolveAfter2Seconds() {
//     return new Promise(resolve => {
//         setTimeout(() => {
//             resolve('resolved');
//         }, 2000);
//     });
// }

// async function asyncCall() {
//     console.log('calling');
//     let result = await resolveAfter2Seconds();
//     console.log(result);
// }

// asyncCall();
// The outcome will be "calling" and then after 2 seconds, "resolved" will be shown.