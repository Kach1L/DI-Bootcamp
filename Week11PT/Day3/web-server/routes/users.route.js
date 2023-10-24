const express = require('express')
const user_router = express.Router();
const { getAllUsers,
    searchUsers,
    getUser,
    createUser,
    updateUser,
    deleteUser } = require('../controllers/users.controller')

// CRUD - READ - GET - get all users
user_router.get("/api/users", getAllUsers);

//CRUD -READ -GET - search for user name - using query
user_router.get("/api/users/search", searchUsers);

//CRUD -READ  -GET - get one user - using params
user_router.get("/api/users/:id", getUser);

//http://example.com/api/users- create a new user - POST
//CRUD - CREATE -POST - create new user - using body
user_router.post("/api/users", createUser);

//CRUD - UPDATE  -PUT - update a user - using params & body
user_router.put("/api/users/:id", updateUser);

//http://example.com/api/users - delete - DELETE
user_router.delete("/api/users/:id", deleteUser);

module.exports = {
    user_router,
};