const button = document.querySelector("#btn");

button.document.addEventListener('click', function () {
    const myApi = 'http://localhost:3000/api/games';
    const theApi = 'https://www.freetogame.com/api/games';
    const dropdown1 = document.querySelector("#dropdown1");
    const dropdown2 = document.querySelector("#dropdown2");
    const selectedValue1 = dropdown1.value;
    const selectedValue2 = dropdown2.value;
    console.log(selectedValue1, selectedValue2);
    const apiDataElement = document.getElementById('api-data');
    // const myApi = 'http://localhost:3000/api/games';
    // const theApi = 'https://www.freetogame.com/api/games';

    const requestOptions = {
            method: 'GET',
            mode: 'no-cors',
    };

    fetch(theApi, requestOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error('GET request failed');
            }
            return response.json();
        })
        .then(data => {
            apiDataElement.textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            console.error('Error:', error);
        });
});