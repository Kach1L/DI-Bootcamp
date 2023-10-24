const express = require('express');
const app = express();
const port = 3000;

app.get('/api/games', (req, res) => {
  // const data = {
  //   message: 'This is your API response.',
  // };
  // res.json(data)

  const apiUrl = 'https://www.freetogame.com/api/games';

  axios.get(apiUrl)
    .then((response) => {

      res.json(response.data);
      console.log('API Response:', response.data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  });

  // Start the server
  app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
  });
