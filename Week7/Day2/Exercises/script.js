// // #1
// const h1 = document.querySelector("h1");
// console.log(h1);

// // #2
// const article = document.querySelector("article");
// const p4 = document.getElementById("p4");
// p4.innerText = "";
// console.log(article);

// // #3
// const h2 = document.querySelector("h2");
// h2.addEventListener("click",()=>{
//     h2.style.backgroundColor = "red";
// });

// // #4
// const h3 = document.querySelector("h3");
// h3.addEventListener("click",()=>{
//     h3.style.display = "none";
// });

// // #5
// const button = document.querySelector("button")
// button.addEventListener("click",()=>{
//     article.style.fontWeight = "bold"
// });

// // #6 BONUS
// h1.addEventListener("mouseover",()=>{
//     num = Math.floor(Math.random()*101)
//     console.log(num);
// });

// // #7 BONUS
// const p2 = document.getElementById("p2");
// p2.addEventListener("mouseover",()=>{
//     p2.classList.toggle("fade");
// });



// EX 2 #1, #2, & #3
// const fname = document.getElementById("fname")
// const lname = document.getElementById("lname")
// const form = document.querySelector("form")
// form.addEventListener("submit",(event)=>{
//     event.preventDefault()
//     console.log(form.fname.value)
//     console.log(form.lname.value)
//     console.log(form.firstname.value)
//     console.log(form.lastname.value)
// });

// #4
// document.addEventListener('DOMContentLoaded', () => {
//     const userForm = document.getElementById('userForm');
//     const usersAnswerList = document.querySelector('.usersAnswer');

//     userForm.addEventListener('submit', function(event) {
//         event.preventDefault();

//         const firstNameInput = document.getElementById('fname');
//         const lastNameInput = document.getElementById('lname');

//         const firstNameValue = firstNameInput.value.trim();
//         const lastNameValue = lastNameInput.value.trim();

//         if (firstNameValue !== '' && lastNameValue !== '') {
//             const firstNameItem = document.createElement('li');
//             firstNameItem.textContent = firstNameValue;

//             const lastNameItem = document.createElement('li');
//             lastNameItem.textContent = lastNameValue;

//             usersAnswerList.innerHTML = ''; // Clear previous entries
//             usersAnswerList.appendChild(firstNameItem);
//             usersAnswerList.appendChild(lastNameItem);

//             // Clear the input fields
//             firstNameInput.value = '';
//             lastNameInput.value = '';
//         }
//     });
// });



// EX 3 #1,2,3,4,5
// document.addEventListener('DOMContentLoaded', () => {
//     let allBoldItems = [];

//     function getBoldItems() {
//         const paragraph = document.querySelector('p');
//         allBoldItems = paragraph.querySelectorAll('strong');
//     }

//     function highlight() {
//         allBoldItems.forEach(item => {
//             item.style.color = 'blue';
//         });
//     }

//     function returnItemsToDefault() {
//         allBoldItems.forEach(item => {
//             item.style.color = 'black';
//         });
//     }

//     getBoldItems();

//     const paragraph = document.querySelector('p');
//     paragraph.addEventListener('mouseover', highlight);
//     paragraph.addEventListener('mouseout', returnItemsToDefault);
// });


// EX 4
// document.addEventListener('DOMContentLoaded', () => {
//     const form = document.getElementById('MyForm');
//     const radiusInput = document.getElementById('radius');
//     const volumeInput = document.getElementById('volume');

//     form.addEventListener('submit', function(event) {
//         event.preventDefault();

//         const radius = parseFloat(radiusInput.value);
//         if (!isNaN(radius)) {
//             const volume = calculateVolume(radius);
//             volumeInput.value = volume.toFixed(2);
//         } else {
//             volumeInput.value = '';
//         }
//     });

//     function calculateVolume(radius) {
//         return (4/3) * Math.PI * Math.pow(radius, 3);
//     }
// });


// EX 5
// document.addEventListener('DOMContentLoaded', () => {
//     const myElement = document.getElementById('myElement');

//     myElement.addEventListener('click', () => {
//         myElement.style.backgroundColor = getRandomColor();
//     });

//     myElement.addEventListener('mouseover', () => {
//         myElement.style.transform = 'translateX(20px)';
//     });

//     myElement.addEventListener('mouseout', () => {
//         myElement.style.transform = 'translateX(0)';
//     });

//     myElement.addEventListener('dblclick', () => {
//         myElement.style.fontSize = '24px';
//     });

//     function getRandomColor() {
//         const letters = '0123456789ABCDEF';
//         let color = '#';
//         for (let i = 0; i < 6; i++) {
//             color += letters[Math.floor(Math.random() * 16)];
//         }
//         return color;
//     }
// });



