const express = require('express');
const router = express.Router();
const fs = require('fs');
const port = 5000;
const tasksFile = 'task.json';

router.use(bodyParser.json());
router.use(bodyParser.urlencoded({ extended: true }));

router.get("/api/tasks", (req, res) => {
  fs.readFile(tasksFile, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).send('Internal Server Error');
    }
    const tasks = JSON.parse(data);
    res.json(tasks);
  });
});
  
router.get("/api/tasks/:id", (req, res) => {
    fs.readFile(tasksFile, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).send('Internal Server Error');
    }

    const { id } = req.params;
    const tasks = JSON.parse(data);
    const task = tasks.find((item) => item.id === id);

    if (!task) {
      return res.status(404).send('Task not found');
    }
    
    res.json(task);
  });
});
  
router.post("/api/tasks", (req, res) => {
  const { work, location } = req.body;

  if (!work || !location) {
    return res.status(400).send('Work and location are required');
  }

  fs.readFile(tasksFile, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).send('Internal Server Error');
    }

    const tasks = JSON.parse(data);
    const newTask = {
      id: tasks.length + 1,
      work,
      location,
    };

    tasks.push(newTask);

    fs.writeFile(tasksFile, JSON.stringify(tasks), (err) => {
      if (err) {
        return res.status(500).send('Internal Server Error');
      }
      res.json(newTask);
    });
  });
});
  
  //CRUD - UPDATE  -PUT - update a user - using params & body
router.put("/api/users/:id", (req, res) => {
  fs.readFile(tasksFile, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).send('Internal Server Error');
    }

    const { id } = req.params;
    const tasks = JSON.parse(data);
    const taskIndex = tasks.findIndex((item) => item.id === id);

    if (taskIndex === -1) {
      return res.status(404).send('Task not found');
    }

    tasks[taskIndex] = { id: id, work, location };

    fs.writeFile(tasksFile, JSON.stringify(tasks), (err) => {
      if (err) {
        return res.status(500).send('Internal Server Error');
      }
      res.json({ id: id, work, location });
    });
  });
});
  
  //http://example.com/api/users - delete - DELETE
router.delete("/api/users/:id", (req, res) => {
//     const { id } = req.params;
//     const index = users.findIndex((item) => item.id == id);
//     if (index === -1) return res.status(404).json({ msg: "user not found" });
//     users.splice(index, 1);
//     res.json(tasks);
// });
const id = req.params;
  if (!id) {
    return res.status(400).send('Invalid task ID');
  }

  fs.readFile(tasksFile, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).send('Internal Server Error');
    }

    const tasks = JSON.parse(data);
    const taskIndex = tasks.findIndex((item) => item.id === id);

    if (taskIndex === -1) {
      return res.status(404).send('Task not found');
    }

    tasks.splice(taskIndex, 1);

    fs.writeFile(tasksFile, JSON.stringify(tasks), (err) => {
      if (err) {
        return res.status(500).send('Internal Server Error');
      }
      res.send('Task deleted successfully');
    });
  });
});


router.listen(port, () =>{
    console.log(`Server is running on port ${port}`);
});

