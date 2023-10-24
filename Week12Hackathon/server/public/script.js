const button = document.getElementById("btn").addEventListener('click', function () {
    const myApi = 'http://localhost:3000/api/games';
    const theApi = 'https://www.freetogame.com/api/games';
    const dropdown1 = document.getElementById("dropdown1");
    const dropdown2 = document.getElementById("dropdown2");
    const selectedValue1 = dropdown1.value;
    const selectedValue2 = dropdown2.value;
    console.log(selectedValue1, selectedValue2);
    const apiDataElement = document.getElementById('api-data');

    const requestOptions = {
        method: 'GET',
        mode: 'no-cors',
};

async function apiRetrieve(api) {
    try {
        const response = await fetch(api, requestOptions); // Replace with your API endpoint URL
        if (!response.ok) {
            throw new Error('API request failed');
        }
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Error:', error);
    }}
apiRetrieve(theApi);
});
