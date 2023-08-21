// document.addEventListener('DOMContentLoaded', () => {
//     const form = document.getElementById('libform');
//     const storySpan = document.getElementById('story');
//     const libButton = document.getElementById('lib-button');

//     form.addEventListener('submit', function(event) {
//         event.preventDefault();

//         const noun = document.getElementById('noun').value.trim();
//         const adjective = document.getElementById('adjective').value.trim();
//         const person = document.getElementById('person').value.trim();
//         const verb = document.getElementById('verb').value.trim();
//         const place = document.getElementById('place').value.trim();

//         if (noun === '' || adjective === '' || person === '' || verb === '' || place === '') {
//             console.log('Please fill in all inputs');
//             return;
//         }

//         const story = `Once upon a time, there was a ${adjective} ${noun} named ${person}. They loved to ${verb} in ${place}.`;
//         storySpan.textContent = story;
//     });

//     libButton.addEventListener('click', function() {
//         storySpan.textContent = ''; // Clear the story
//     });
// });
