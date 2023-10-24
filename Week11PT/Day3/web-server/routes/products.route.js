const express = require('express')
const products_router = express.Router();
const {
     getAllProducts,
     getProduct } = require('../controllers/products.controller')

// CRUD - READ - GET - get all users
products_router.get("/api/users", getAllProducts);

//CRUD -READ -GET - search for user name - using query
products_router.get("/api/users/search", (req, res) => {
  const { name } = req.query;
  const filtered_users = users.filter((item) =>
    item.name.toLowerCase().includes(name.toLowerCase())
  );
  if (filtered_users.length === 0)
    return res.status(404).json({ msg: "users not found" });
  res.json(filtered_users);
});

//CRUD -READ  -GET - get one user - using params
products_router.get("/api/users/:id", getProduct);

//http://example.com/api/users- create a new user - POST
//CRUD - CREATE -POST - create new user - using body
products_router.post("/api/users", (req, res) => {
  console.log("body=>", req.body);
  const { name, email } = req.body;
  const newUser = {
    id: users.length + 1,
    name,
    email,
  };
  users.push(newUser);
  res.json(users);
});

//CRUD - UPDATE  -PUT - update a user - using params & body
products_router.put("/api/users/:id", (req, res) => {
  const { id } = req.params;
  const { name, email } = req.body;
  const index = users.findIndex((item) => item.id == id);

  if (index === -1) return res.status(404).json({ msg: "user not found" });

  users[index].name = name;
  users[index].email = email;

  res.json(users);
});

//http://example.com/api/users - delete - DELETE
products_router.delete("/api/users/:id", (req, res) => {
  const { id } = req.params;
  const index = users.findIndex((item) => item.id == id);
  if (index === -1) return res.status(404).json({ msg: "user not found" });
  users.splice(index, 1);
  res.json(users);
});

module.exports = {
    products_router,
};