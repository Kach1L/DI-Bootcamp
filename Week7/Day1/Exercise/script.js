// Ex 1
// function displayNumbersDivisible(divisor){
//     let sum = 0;

//     for (let i=0;i<=500;i++){
//         if (i%divisor === 0){
//         sum += i
//         }
//     }
//     console.log(`Sum of numbers divisible by ${divisor}: ${sum}`);
// }

// displayNumbersDivisible(3)

// Ex 2
// const stock = {
//     "banana": 6,
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry": 1
// };

// const prices = {
//     "banana": 4,
//     "apple": 2,
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry": 10
// };

// const shoppingList = ["banana", "orange", "apple"];

// function myBill() {
//     let total = 0;

//     for (let item of shoppingList) {
//         if (item in stock && stock[item] > 0) {
//             total += prices[item];
//             stock[item]--; // Decrease the item's stock by 1
//         }
//     }

//     return total;
// }

// const totalPrice = myBill();
// console.log("Total price of shopping list:", totalPrice);
// console.log("Updated stock:", stock);


// Ex 3
// function changeEnough(itemPrice, amountOfChange) {
//     const quarterValue = 0.25;
//     const dimeValue = 0.10;
//     const nickelValue = 0.05;
//     const pennyValue = 0.01;

//     // Calculate the total change in dollars
//     const totalChange = (amountOfChange[0] * quarterValue) +
//                         (amountOfChange[1] * dimeValue) +
//                         (amountOfChange[2] * nickelValue) +
//                         (amountOfChange[3] * pennyValue);

//     return totalChange >= itemPrice;
// }

// Test cases
// console.log(changeEnough(4.25, [25, 20, 5, 0])); // Should return true
// console.log(changeEnough(14.11, [2, 100, 0, 0])); // Should return false
// console.log(changeEnough(0.75, [0, 0, 20, 5])); // Should return true


// Ex 4
// function hotelCost() {
//     let numNights;
//     while (true) {
//         numNights = prompt("Enter the number of nights you'd like to stay in the hotel:");
//         if (numNights === null) {
//             return; // Exit if the user cancels
//         }
//         numNights = parseInt(numNights);
//         if (!isNaN(numNights)) {
//             break;
//         }
//     }
//     return numNights * 140;
// }

// function planeRideCost() {
//     let destination;
//     while (true) {
//         destination = prompt("Enter your destination:");
//         if (destination === null) {
//             return; // Exit if the user cancels
//         }
//         if (typeof destination === "string" && destination.trim() !== "") {
//             break;
//         }
//     }
//     switch (destination.toLowerCase()) {
//         case "london":
//             return 183;
//         case "paris":
//             return 220;
//         default:
//             return 300;
//     }
// }

// function rentalCarCost() {
//     let numDays;
//     while (true) {
//         numDays = prompt("Enter the number of days you'd like to rent the car:");
//         if (numDays === null) {
//             return; // Exit if the user cancels
//         }
//         numDays = parseInt(numDays);
//         if (!isNaN(numDays)) {
//             break;
//         }
//     }
//     let cost = numDays * 40;
//     if (numDays > 10) {
//         cost *= 0.95; // Apply 5% discount for more than 10 days
//     }
//     return cost;
// }

// function totalVacationCost() {
//     const hotel = hotelCost();
//     const plane = planeRideCost();
//     const car = rentalCarCost();

//     if (hotel !== undefined && plane !== undefined && car !== undefined) {
//         const total = hotel + plane + car;
//         console.log("Total vacation cost: $" + total);
//     } else {
//         console.log("Vacation cost calculation canceled.");
//     }
// }

// // Call the totalVacationCost() function to calculate and display the total cost
// totalVacationCost();


// Ex 5
// // Retrieve the div and console.log it
// const container = document.getElementById('container');
// console.log(container);

// // Change the name "Pete" to "Richard"
// const peteElement = document.querySelector('.list:nth-child(1) li:nth-child(2)');
// peteElement.textContent = "Richard";// I dont understand how the error here, couldnt find the solution

// // Delete the second <li> of the second <ul>
// const secondList = document.querySelector('.list:nth-child(2)');
// const danElement = secondList.querySelector('li:last-child');
// secondList.removeChild(danElement);

// // Change the name of the first <li> of each <ul> to your name
// const ulElements = document.querySelectorAll('.list');
// ulElements.forEach(ul => {
//     const firstLi = ul.querySelector('li:first-child');
//     firstLi.textContent = "Your Name";
// });

// // Add classes to <ul> and <li> elements
// ulElements.forEach(ul => {
//     ul.classList.add('student_list');
// });
// ulElements[0].classList.add('university', 'attendance');

// // Add styles and perform other manipulations
// container.style.backgroundColor = 'lightblue';
// container.style.padding = '10px';

// const danLi = document.querySelector('.list:nth-child(1) li:last-child');
// danLi.style.display = 'none';

// const richardLi = document.querySelector('.list:nth-child(1) li:nth-child(2)');
// richardLi.style.border = '1px solid black';

// document.body.style.fontSize = '16px';

// // Bonus: Check background color and alert
// if (container.style.backgroundColor === 'lightblue') {
//     const users = document.querySelectorAll('.list li');
//     let usersText = '';
//     users.forEach(user => {
//         usersText += user.textContent + ' and ';
//     });
//     usersText = usersText.slice(0, -5); // Remove the last " and "
//     alert(`Hello ${usersText}`);
// }


// Ex 6
// Change the value of the id attribute from navBar to socialNetworkNavigation
// const navBar = document.getElementById('navBar');
// navBar.setAttribute('id', 'socialNetworkNavigation');

// // Create a new <li> element and text node for "Logout"
// const newLi = document.createElement('li');
// const newText = document.createTextNode('Logout');
// newLi.appendChild(newText);

// // Append the new <li> element to the <ul>
// const ul = navBar.querySelector('ul');
// ul.appendChild(newLi);

// // Retrieve and display the text of the first and last <li> elements
// const firstLi = ul.firstElementChild;
// const lastLi = ul.lastElementChild;

// console.log("Text of the first link:", firstLi.textContent);
// console.log("Text of the last link:", lastLi.textContent);


// Ex 7
// Create an array of book objects
const allBooks = [
    {
        title: "Harry Potter",
        author: "J.K. Rowling",
        image: "https://m.media-amazon.com/images/I/71HbYElfY0L._AC_UF1000,1000_QL80_.jpg",
        alreadyRead: true
    },
    {
        title: "The Great Gatsby",
        author: "F. Scott Fitzgerald",
        image: "https://m.media-amazon.com/images/I/81DAU6LzKKL._AC_UF1000,1000_QL80_.jpg",
        alreadyRead: false
    }
];

// Get the section where books will be displayed
const listBooksSection = document.querySelector('.listBooks');

// Loop through the array and render each book
allBooks.forEach(book => {
    const bookDiv = document.createElement('div');
    const bookTitle = document.createElement('p');
    const bookAuthor = document.createElement('p');
    const bookImage = document.createElement('img');

    bookTitle.textContent = `${book.title} written by ${book.author}`;
    bookAuthor.textContent = book.alreadyRead ? "Already read" : "Not read yet";
    bookImage.src = book.image;
    bookImage.style.width = "100px";

    if (book.alreadyRead) {
        bookTitle.style.color = "red";
        bookAuthor.style.color = "red";
    }

    bookDiv.appendChild(bookTitle);
    bookDiv.appendChild(bookAuthor);
    bookDiv.appendChild(bookImage);
    listBooksSection.appendChild(bookDiv);
});

