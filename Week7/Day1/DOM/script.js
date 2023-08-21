//DOM selecting elements

// const myHeader = document.querySelector("h1");
// console.log(myHeader.innerText);
// myHeader.innerText = "WELCOME TO MY PAGE!!!!! SO EXCITED TO HAVE YOU!!!! :D";

// const myList = document.querySelector("ul");
// console.log(myList.firstElementChild);
// myList.firstElementChild.innerText = "BANANA";

// console.log(myList.parentElement);

// const myP = document.querySelector("#secondP");
// console.log(myP.textContent);

// const myP = document.getElementById("secondP");
// console.log(myP.textContent);

// const myh2 = document.querySelector(".red");
// console.log(myh2);

// // const myDiv = document.querySelectorAll("div");
// // console.log(myDiv);
// const myDiv = document.querySelector("div");
// const newHeader = document.createElement("h2");
// // const header=document.querySelector("#h1");
// // const headerText = document.createTextNode("This is a new header");

// // newHeader.append(headerText);

// newHeader.innerText = "This is a new header";
// myDiv.append(newHeader);

// newHeader.style.backgroundColor = "pink";
// myDiv.style.border = "1px solid red";

// newHeader.classList = "red";
// // myDiv.remove();

// //Attributes
// const header = document.getElementById("firstHeader");

// //Check if I have an attribute
// console.log(header.hasAttribute("id"));

// //Get Attribute
// console.log(header.getAttribute("id"));

// console.log(header.id);

//Set Attribute

// header.setAttribute("style", "color:yellow;");
// header.style.color = "pink";
// header.className = "banana pear apple";
// header.classList.add("red", "border");

// console.log(header.classList.contains("redd"));

//Forms
// const form1 = document.querySelector("form");
// console.log(form1);

// const forms = document.forms;
// console.log(forms[0]);
// console.log(forms[1]);
// console.log(forms.my);
// console.log(forms.yours.elements.one);
// const myInput = document.getElementById("one");
// console.log(myInput.value);
const todoList = document.getElementById("todoList");
const myInput = document.getElementById("one");
console.log(myInput.form);
console.log(todoList);

function addToTodoList() {
  if (myInput.value.length < 1) {
    alert("Please fill a task");
  } else {
    const newLi = document.createElement("li");
    newLi.innerText = myInput.value;
    todoList.append(newLi);
    myInput.value = "";
  }
}

const mySelect = document.querySelector("select");

function selected() {
  console.log(mySelect.value);
}
