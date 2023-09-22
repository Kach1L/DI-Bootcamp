// const slugify = require('slugify');
const axios = require('axios');
// const link = slugify('about page')
// console.log(link);


const getData = async (url) => {
    try{
        const res = await axios.get(url);
        return res.data;
    } catch(error){
        console.log(error);
    }
};

module.exports = {
    getData
};


// if (!fetchJson.ok) {
     
// } else{
//     const proJson = fetch(fetchJson);
//     console.log(proJson);
// }