// Ex 1
// Part I
// setTimeout(function() {
//     alert("Hello World - Part I");
// }, 2000);

// // Part II
// setTimeout(function() {
//     const container = document.getElementById('container');
//     const newParagraph = document.createElement('p');
//     newParagraph.textContent = 'Hello World - Part II';
//     container.appendChild(newParagraph);
// }, 2000);

// // Part III
// const interval = setInterval(function() {
//     const container = document.getElementById('container');
//     const newParagraph = document.createElement('p');
//     newParagraph.textContent = 'Hello World - Part III';
//     container.appendChild(newParagraph);

//     if (container.childElementCount === 5) {
//         clearInterval(interval);
//     }
// }, 2000);

// const clearButton = document.getElementById('clear');
// clearButton.addEventListener('click', function() {
//     clearInterval(interval);
// });


// Ex 2
function myMove() {
    const container = document.getElementById('container');
    const animate = document.getElementById('animate');
    
    let position = 0;
    const interval = setInterval(frame, 1); // Move 1px every millisecond

    function frame() {
        if (position >= container.clientWidth - animate.clientWidth) {
            clearInterval(interval); // Stop the animation
        } else {
            position++;
            animate.style.left = position + 'px'; // Update the position
        }
    }
}
