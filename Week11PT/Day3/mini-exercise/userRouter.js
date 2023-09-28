const express = require('express');
const router = express.Router();
const fs = require('fs')

const taskJson = 'task.json';

router.get("/api/tasks", (req, res) => {
    res.json(tasks);
  });
  
router.get("/api/tasks/:id", (req, res) => {
    // console.log("params=>", req.params);
    const { id } = req.params;
    const task = tasks.find((item) => item.id == id);
    if (!task) return res.status(404).json({ msg: "user not found" });
    res.json(tasks);
});
  
router.post("/api/tasks", (req, res) => {
    console.log("body=>", req.body);
    const { name, email } = req.body;
    const newTask = {
      id: tasks.length + 1,
      work,
      location,
    };
    users.push(newTask);
    res.json(tasks);
  });
  
  //CRUD - UPDATE  -PUT - update a user - using params & body
router.put("/api/users/:id", (req, res) => {
    const { id } = req.params;
    const { name, email } = req.body;
    const index = users.findIndex((item) => item.id == id);
  
    if (index === -1) return res.status(404).json({ msg: "user not found" });
  
    users[index].name = name;
    users[index].email = email;
  
    res.json(tasks);
});
  
  //http://example.com/api/users - delete - DELETE
router.delete("/api/users/:id", (req, res) => {
    const { id } = req.params;
    const index = users.findIndex((item) => item.id == id);
    if (index === -1) return res.status(404).json({ msg: "user not found" });
    users.splice(index, 1);
    res.json(tasks);
});