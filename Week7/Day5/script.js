const robots = [
    {
      id: 1,
      name: 'Leanne Graham',
      username: 'Bret',
      email: 'Sincere@april.biz',
      image: 'R1.PNG'
    },
    {
      id: 2,
      name: 'Ervin Howell',
      username: 'Antonette',
      email: 'Shanna@melissa.tv',
      image: 'R2.PNG'
    },
    {
      id: 3,
      name: 'Clementine Bauch',
      username: 'Samantha',
      email: 'Nathan@yesenia.net',
      image: 'R3.PNG'
    },
    {
      id: 4,
      name: 'Patricia Lebsack',
      username: 'Karianne',
      email: 'Julianne.OConner@kory.org',
      image: 'R4.PNG'
    },
    {
      id: 5,
      name: 'Chelsey Dietrich',
      username: 'Kamren',
      email: 'Lucio_Hettinger@annie.ca',
      image: 'R5.PNG'
    },
    {
      id: 6,
      name: 'Mrs. Dennis Schulist',
      username: 'Leopoldo_Corkery',
      email: 'Karley_Dach@jasper.info',
      image: 'R6.PNG'
    },
    {
      id: 7,
      name: 'Kurtis Weissnat',
      username: 'Elwyn.Skiles',
      email: 'Telly.Hoeger@billy.biz',
      image: 'R7.PNG'
    },
    {
      id: 8,
      name: 'Nicholas Runolfsdottir V',
      username: 'Maxime_Nienow',
      email: 'Sherwood@rosamond.me',
      image: 'R8.PNG'
    },
    {
      id: 9,
      name: 'Glenna Reichert',
      username: 'Delphine',
      email: 'Chaim_McDermott@dana.io',
      image:'R9.PNG'
    },
    {
      id: 10,
      name: 'Clementina DuBuque',
      username: 'Moriah.Stanton',
      email: 'Rey.Padberg@karina.biz',
      image:'R10.PNG'
    }
    ];

// console.log(robots)

// Creating DOM Objects
const head = document.createElement("h2");
head.innerText = "Robo-Researcher";
const roboNav = document.getElementById("roboNav");
const searchBar = document.createElement("input");
const roboCards = document.getElementById("container");


// Specifying the Content
head.innerText = "Robo-Researcher";


// Styling the Page
searchBar.type = "text";
searchBar.placeholder = "Make Robo-Search"
roboNav.appendChild(head);
roboNav.appendChild(searchBar);
roboNav.style.backgroundImage = "url(gears.jpg)";

roboNav.style.display = "flex";
roboNav.style.flexWrap = "wrap";
head.style.paddingTop = "15px";
head.style.paddingRight = "20px";
head.style.fontFamily = "h Hack Glitch";
head.style.fontSize = "30px";
head.style.color = "white"; 

searchBar.style.marginTop = "10px";
searchBar.style.marginBottom = "20px";
searchBar.style.paddingTop = "10px";
searchBar.style.paddingBottom = "5px";

roboCards.style.display = "flex";
roboCards.style.flexWrap = "wrap";
roboCards.style.justifyContent = "center";
roboCards.style.alignItems = "center"


// function displayRobots() {
//     // console.log(robots)
//     robots.forEach((robo,i,arr) => {
//         const card = document.createElement("div");
//         card.className = "card";
        
//         const roboImage = document.createElement("img");
//         roboImage.src = robo.image;

//         const roboName = document.createElement("h3");
//         roboName.innerText = robo.name;

//         const roboEmail = document.createElement("p");
//         roboEmail.innerText = robo.email;

//         card.append(roboImage,roboName,roboEmail);
//         roboCards.append(card);
//     });
// }
// displayRobots()

console.log(roboCards);
searchBar.addEventListener("input",() => {filterRobots(robots)});

function filterRobots(robotArray) {
    roboCards.innerHTML = ""
    robotArray.filter((ele) => {
        return ele.name.toLowerCase().includes(searchBar.value.toLowerCase())
    }).forEach((robo,i,arr) => {
        const card = document.createElement("div");
        card.className = "card";
        
        const roboImage = document.createElement("img");
        roboImage.src = robo.image;

        const roboName = document.createElement("h3");
        roboName.innerText = robo.name;

        const roboEmail = document.createElement("p");
        roboEmail.innerText = robo.email;
        
        card.append(roboImage,roboName,roboEmail);
        roboCards.append(card);
        })
    };
filterRobots(robots);
// const res = roboCards.filter((roboCards) => {
//     roboCards.name.toLowerCase[0,2] == searchBar.toLowerCase[0,2]
//     return roboCards;
// });