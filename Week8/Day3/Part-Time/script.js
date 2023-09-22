// function testSolution() {
//     const testCases = [
//       { input: 'aabbb', output: true },
//       { input: 'ba', output: false },
//       { input: 'aaa', output: true },
//       { input: 'b', output: true },
//       { input: 'abba', output: false },
//       { input: 'a', output: true },
//       { input: 'bbaa', output: false },
//       { input: 'bbba', output: false },
//       { input: 'aabb', output: true },
//       { input: 'bababab', output: false },
//       { input: 'babababa', output: false },
//       { input: 'aabababb', output: false },
//       { input: 'baaab', output: false },
//       { input: 'bbabbabbababbab', output: false },
//       { input: 'babaabaaab', output: false },
//       { input: 'ab', output: true },
  
  
//     ];
  
//     for (let i = 0; i < testCases.length; i++) {
//       const { input, output } = testCases[i];
//       const result = solution(input);
//       console.log(`Input: "${input}", Output: ${result}, Expected Output: ${output}`);
//     }
//   }
  
// testSolution();

// function solution(S) {
//     let len = S.length;
  
//     let lastAIndex = -1;
//     let lastBIndex = -1;
    
//     for (let i = 0; i < len; i++) {
//       if (S[i] === "a") {
//         lastAIndex = i;
//       } else if (S[i] === "b") {
//         lastBIndex = i;
//       }
//       if (lastBIndex < lastAIndex && lastBIndex !== -1 && lastAIndex !== -1) {
//         console.log(false);
//         return false;
//       }
//     }
//     console.log(true);
//     return true;
// }




// XMLHttpRequest

// let xhr = new XMLHttpRequest();

// // console.log("xhr=>", xhr);

// // xhr.open("GET", "https://jsonplaceholder.typicode.com/users");
// xhr.open("GET", "https://zivuch.github.io/load?999999");

// // xhr.timeout = 10000;
// // type
// // ""
// // text
// // json
// // document
// // xhr.responseType = "document"

// xhr.send();

// xhr.onload = () => {
//   if (xhr.status === 200)
//     console.log(xhr.response); //zivuch(xhr.response);//render(xhr.response);
//   else console.log(`${xhr.status} : ${xhr.statusText} `);
// };

// xhr.onerror = () => {
//   console.log("Request failed");
// };

// xhr.onprogress = (event) => {
//   if (event.lengthComputable) {
//     console.log(`Received ${event.loaded} of ${event.total} bytes`);
//   } else {
//     console.log(`Received ${event.loaded} bytes`); // no Content-Length
//   }
// };

// const render = (arr) => {
//   console.log(arr);
//   const html = arr.map((item) => {
//     return `<div style="display:inline-block;margin:20px;border:1px solid cyan;padding:20px;text-align:center;">
//       <img src=https://robohash.org/${item.id}?size=150x150 />
//       <h2>${item.name}</h2>
//       <p>${item.username}</p>
//       <p>${item.email}</p>
//     </div>`;
//   });
//   document.getElementById("root").innerHTML = html.join("");
//   console.log(html);
// };

// function zivuch(xmlDoc) {
//   var cd = xmlDoc.getElementsByTagName("email");
//   for (let i = 0; i < cd.length; i++) {
//     console.log(cd[i].getElementsByTagName("to")[0].childNodes[0].nodeValue);
//     console.log(cd[i].getElementsByTagName("from")[0].childNodes[0].nodeValue);
//   }
// }



const data = null;

const xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener('readystatechange', function () {
	if (this.readyState === this.DONE) {
		console.log(JSON.parse(this.responseText));
	}
});

xhr.open('GET', 'https://weatherapi-com.p.rapidapi.com/current.json?q=53.1%2C-0.13');
xhr.setRequestHeader('X-RapidAPI-Key', 'c3c01484f9msh9602576cd222b48p10c6fdjsnecff5bb48a0a');
xhr.setRequestHeader('X-RapidAPI-Host', 'weatherapi-com.p.rapidapi.com');

xhr.send(data);