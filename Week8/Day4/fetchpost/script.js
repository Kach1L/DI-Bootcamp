const newPost = {
    title : "An article about Javascript",
    body : "Js is great !!!",
    userId : 1
}

// https://jsonplaceholder.typicode.com/guide/

async function addData () {
    try {
        const url = `https://jsonplaceholder.typicode.com/posts`
        const resp = await fetch (url , {
            method : "POST",
            body : JSON.stringify(newPost),
            headers: {
                'Content-Type': 'application/json; charset=UTF-8'
            }
        })
        if (!resp.ok) {
            throw new Error("oops")
        } else {
            const data = await resp.json();
            console.log("The data received is ", data);
        }
    } catch (err) {
        console.log(err);
    }
    
    
}

addData()