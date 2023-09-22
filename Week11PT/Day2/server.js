const express = require('express');
const bodyParser = require('body-parser');
const {users} = require("./config/users.js")

// create application/json parser
const jsonParser = bodyParser.json()

// create application/x-www-form-urlencoded parser
const urlencodedParser = bodyParser.urlencoded({ extended: false })

const app = express();

app.get('/', (req,res)=>{
    res.send('<h1>Home</h1>')
});

app.get('/about', (req,res)=>{
    res.send('<h1>About</h1>')
});

// app.get('*', (req,res)=>{
//     res.send('<h1>404</h1>')
// });

app.listen(3001, ()=>{
    console.log("run on port 3001");
})

app.get('/api/users', (req,res)=>{
    res.json(users);
});

app.get('/api/users/:id', (req,res)=>{
    const userId = req.params;
});

app.get('/api/users/search', (req,res)=>{
    const { name } = req.query;
    const filtered_users = users.filter((item) => item.name.toLowerCase.includes(name.toLowerCase()))
    if (filtered_users.length === 0)
        return res.status(404).json({msg: 'users not found'});
    res.json(filtered_users);
});

app.post("/api/users", (req, res)=>{
    res.json(`You have added ${req.body}`)
    users = users + req.body

})