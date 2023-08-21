//Event Listeners

// function clicked() {
//   alert("Button was clicked");
// }

// function mouseOver() {
//   console.log("mouseover event fired");
// }

// const button = document.getElementById("clickEvent");

// const innerDiv = document.querySelector("#innerDiv");
// button.addEventListener("click", clicked);

// button.addEventListener("click", function click() {
//   alert("Clicked button");
// });

// button.addEventListener("click", () => {
//   button.style.backgroundColor = "red";
// });

// button.onclick = clicked;

// button.onmouseover = mouseOver;
// innerDiv.onmouseout = mouseOver;

//Exercise 1

// const table = document.getElementById("sampleTable");
// let row = 2;
// function insertRow() {
//   row++;
//   const newRow = document.createElement("tr");
//   const td1 = document.createElement("td");
//   const td2 = document.createElement("td");
//   td1.innerText = `Row${row} cell1`;
//   td2.innerText = `Row${row} cell2`;
//   newRow.append(td1, td2);
//   table.append(newRow);
// }
// const innerDiv = document.getElementById("innerDiv");

// innerDiv.addEventListener("click", RespondClick);

// innerDiv.addEventListener("mouseover", RespondMouseOver);

// innerDiv.addEventListener("mouseout", RespondMouseOut);

// function RespondClick(e) {
//   console.log(e.target);
// }

// function RespondMouseOver() {
//   console.log("My mouse is over the btn");
// }

// function RespondMouseOut() {
//   console.log("My mouse is out of the btn");
// }

// const myInput = document.getElementById("myInput");

// myInput.oninput = function (e) {
//   innerDiv.innerText = e.target.value;
// };
// const parentDiv = document.getElementById("parent");
// const childDiv = document.getElementById("child");
// const infantDiv = document.getElementById("infant");
// parentDiv.style.height = "300px";
// childDiv.style.height = "200px";
// infantDiv.style.height = "100px";
// parentDiv.style.border = "1px solid red";
// childDiv.style.border = "1px solid blue";
// infantDiv.style.border = "1px solid green";
// parentDiv.onclick = () => console.log("parent");
// childDiv.onclick = () => console.log("child");
// infantDiv.onclick = () => console.log("infant");
// const myvalue = (document.forms[0].elements.firstFormInput.value = "hello i am value");
// console.log(myvalue);

// function getvalue(event) {
//   event.preventDefault();
//   console.log(event);
//   console.log(event.target.elements.fname.value);
//   console.log(event.target.elements.lname.value);
// }
// const button = document.querySelector("button");
// function clickme(e) {
//   console.log(e);
// }

// button.addEventListener("click", clickme);

// let dropdown = document.getElementById("A");
// console.log(dropdown);
// dropdown.selectedIndex = 1;
// let inputs = table.getElementsByTagName("input");
// console.log(inputs);
// for (let input of inputs) {
//   console.log(input.value + ": " + input.checked);
// }

// const form = document.getElementsByTagName("form")[0];
// const email = document.getElementById("mail");
// const name = document.getElementById("name");

// email.addEventListener("input", function (event) {
//   if (email.validity.typeMismatch) {
//     email.setCustomValidity("Terrible work");
//   } else {
//     email.setCustomValidity("");
//   }
// });

// form.addEventListener("submit", function (event) {
//   if (!email.validity.valid) {
//     email.setCustomValidity("Terrible work");
//   } else {
//     email.setCustomValidity("");
//   }
// });

//TIMEOUT
// function testTimeout() {
//   alert("after 7 seconds");
// }

// setTimeout(() => {
//   const div = document.createElement("div");
//   div.innerText = "Sale ends in 10 mins";
//   document.body.append(div);
// }, 5000);

// const timeoutId = setTimeout(function () {
//   alert("after 5 seconds");
// }, 5000);

// setTimeout(testTimeout, 7000);

// clearTimeout(timeoutId);
// let num = 0;
// const intervalId = setInterval(() => {
//   num++;
//   const div = document.createElement("div");
//   div.innerText = "interval number " + num;
//   document.getElementById("container").append(div);
// }, 500);
// const button = document.getElementById("button");
// button.addEventListener("click", function () {
//   clearInterval(intervalId);
// });

// function getRandomColor() {
//     const letters = "0123456789ABCDEF";
//     let color = "#";
//     for (let i = 0; i < 6; i++) {
//       color += letters[Math.floor(Math.random() * 16)];
//     }
//     return color;
// }

// const child = document.getElementById("child");

// child.style.left = "0px";
// let position = 0;
// const intervalId = setInterval(() => {
//   if (position === 300) {
//     clearInterval(intervalId);
//   } else {
//     child.style.backgroundColor = getRandomColor();
//     position++;
//     child.style.left = position + "px";
//     child.style.top = position + "px";
//   }
// }, 50);
