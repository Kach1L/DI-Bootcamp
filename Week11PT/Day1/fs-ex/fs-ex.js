const fs = require("fs")

console.log('before');
// const data = fs.readFileSync('info.json', 'utf-8');
// console.log(data);
// fs.readFile('info.json', 'utf-8', (err,data) => {
//     if(err) return console.log(err)
//     console.log(data);
// });
// console.log('after');

// const users = [{ name: "John"}, { name: "Henry"}]

// fs.writeFile('info', JSON.stringify(users) , 'utf-8', (err) => {
//     if(err) return console.log(err)
// });

fs.copyFile('info.json', '../npm-ex/kachi.json' , (err) => {
    if(err) return console.log(err)
});