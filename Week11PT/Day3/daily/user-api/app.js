const express = require('express');
// const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const fs = require('fs');
const app = express();
const port = 3000;
const usersFile = 'user.json';

// parse application/x-www-form-urlencoded
app.use(express.urlencoded({ extended: false }));

// parse application/json
app.use(express.json());

app.post('/register', (req, res) => {
  const { username, password } = req.body;

  if (!username || !password) {
    return res.status(400).json({ message: 'Username and password are required.' });
  }

  fs.readFile(usersFile, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).json({ message: 'Internal Server Error' });
    }

    const users = JSON.parse(data);
    if (users.find((user) => user.username === username)) {
      return res.status(409).json({ message: 'Username already exists.' });
    }

    bcrypt.hash(password, 10, (err, hashedPassword) => {
      if (err) {
        return res.status(500).json({ message: 'Internal Server Error' });
      }

      const newUser = {
        username,
        password: hashedPassword,
      };

      users.push(newUser);
      fs.writeFile(usersFile, JSON.stringify(users), (err) => {
        if (err) {
          return res.status(500).json({ message: 'Internal Server Error' });
        }
        res.status(201).json({ message: 'User registered successfully.' });
      });
    });
  });
});

app.post('/login', (req, res) => {
  const { username, password } = req.body;

  if (!username || !password) {
    return res.status(400).json({ message: 'Username and password are required.' });
  }

  fs.readFile(usersFile, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).json({ message: 'Internal Server Error' });
    }

    const users = JSON.parse(data);
    const user = users.find((u) => u.username === username);

    if (!user) {
      return res.status(401).json({ message: 'Invalid username or password.' });
    }

    bcrypt.compare(password, user.password, (err, result) => {
      if (err || !result) {
        return res.status(401).json({ message: 'Invalid username or password.' });
      }

      res.status(200).json({ message: 'Login successful.' });
    });
  });
});

app.get('/users', (req, res) => {
  fs.readFile(usersFile, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).json({ message: 'Internal Server Error' });
    }

    const users = JSON.parse(data);
    res.status(200).json(users);
  });
});

app.get('/users/:id', (req, res) => {
  const userId = req.params.id;
  fs.readFile(usersFile, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).json({ message: 'Internal Server Error' });
    }

    const users = JSON.parse(data);
    const user = users.find((u) => u.username === userId);

    if (!user) {
      return res.status(404).json({ message: 'User not found.' });
    }

    res.status(200).json(user);
  });
});

app.put('/users/:id', (req, res) => {
  // Update a user's information by ID
  const userId = req.params.id;
  const { username, password } = req.body;

  // Validate input
  if (!username || !password) {
    return res.status(400).json({ message: 'Username and password are required.' });
  }

  fs.readFile(usersFile, 'utf8', (err, data) => {
    if (err) {
      return res.status(500).json({ message: 'Internal Server Error' });
    }

    const users = JSON.parse(data);
    const userIndex = users.findIndex((u) => u.username === userId);

    if (userIndex === -1) {
      return res.status(404).json({ message: 'User not found.' });
    }

    // Hash the new password
    bcrypt.hash(password, 10, (err, hashedPassword) => {
      if (err) {
        return res.status(500).json({ message: 'Internal Server Error' });
      }

      // Update user information
      users[userIndex] = {
        username,
        password: hashedPassword,
      };

      fs.writeFile(usersFile, JSON.stringify(users), (err) => {
        if (err) {
          return res.status(500).json({ message: 'Internal Server Error' });
        }
        res.status(200).json({ message: 'User updated successfully.' });
      });
    });
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
