// const morseJSON = `{
//     "0": "-----",
//     "1": ".----",
//     // ... (other morse codes)
//     ")": "-.--.-"
//   }`;
  
//   function toJs() {
//     return new Promise((resolve, reject) => {
//       try {
//         const morseJS = JSON.parse(morseJSON);
//         if (Object.keys(morseJS).length === 0) {
//           reject("Morse JavaScript object is empty.");
//         } else {
//           resolve(morseJS);
//         }
//       } catch (error) {
//         reject("Error parsing morse JSON: " + error);
//       }
//     });
//   }
  
//   function toMorse(morseJS) {
//     return new Promise((resolve, reject) => {
//       const userWord = prompt("Enter a word or sentence:");
//       const morseTranslation = [];
  
//       for (const char of userWord) {
//         if (char.toLowerCase() in morseJS) {
//           morseTranslation.push(morseJS[char.toLowerCase()]);
//         } else {
//           reject("Character not found in morse JS object: " + char);
//         }
//       }
  
//       resolve(morseTranslation);
//     });
//   }
  
//   function joinWords(morseTranslation) {
//     const morseText = morseTranslation.join(" / ");
//     console.log(morseText);
//     // Display on DOM or wherever needed
//   }
  
//   // Chain the three functions
//   toJs()
//     .then(morseJS => toMorse(morseJS))
//     .then(morseTranslation => joinWords(morseTranslation))
//     .catch(error => console.log("Error:", error));
  