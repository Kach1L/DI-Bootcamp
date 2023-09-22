const axios = require('axios')
const {getData} = require("./app.js");
getData("https://jsonplaceholder.typicode.com/posts").then((data) => console.log(data))