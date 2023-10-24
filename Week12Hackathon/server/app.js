const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();

app.use('/site',express.static(path.join(__dirname, '/public')));

app.get('/api/games', (req, res) => {
    const apiUrl = 'https://www.freetogame.com/api/games?platform=browser&category=mmorpg&sort-by=release-date';

    axios.get(apiUrl)
      .then((response) => {
  
        res.json(response.data);
        // console.log('API Response:', response.data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    });

app.use((req, res) => {
    res.status('404');
    res.send('<h1> Error 404: Resource Not Found </h1>')
})

app.listen(3000, () => {
    console.log("App will listen on port 3000");
});