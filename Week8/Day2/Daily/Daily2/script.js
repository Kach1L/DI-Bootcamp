divContainer = document.getElementById("formCase")  
form1 = document.createElement("form");
fnameInput = document.createElement("input");
lnameInput = document.createElement("input");
button1 = document.createElement("button");

button1.innerHTML = "Send";

function appendAll(){
    divContainer.append(form1);
    form1.append(fnameInput,lnameInput,button1);
}
appendAll()

button1.addEventListener("click",retrieveJson);

function retrieveJson(e){
    e.preventDefault()
    if (fnameInput.value.length == 0 || lnameInput.value.length == 0){
        console.log({"name":NaN,"lastName":NaN});
        console.log("Fill all inputs for results.");
        return {"name":NaN,"lastName":NaN}
    }
    else{
        console.log({"name":fnameInput.value,"lastName":lnameInput.value});
        return {"name":fnameInput.value,"lastName":lnameInput.value}
    }
}