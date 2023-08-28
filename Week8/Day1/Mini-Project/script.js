const colorGrid = document.getElementById('color-grid');
const colorInput = document.getElementById('color-input');
let isDrawing = false;

// Create the color grid
function createColorGrid() {
    for (let i = 0; i < 400; i++) {
        const square = document.createElement('div');
        square.addEventListener('mousedown', startDrawing);
        square.addEventListener('mouseover', draw);
        colorGrid.appendChild(square);
    }
}

function startDrawing() {
    isDrawing = true;
    draw();
}

function stopDrawing() {
    isDrawing = false;
}

function draw(e) {
    if (!isDrawing) return;
    const square = e ? e.target : this;
    square.style.backgroundColor = colorInput.value;
}

colorInput.addEventListener('input', () => {
    draw(); // Update color immediately when user changes color
});

colorGrid.addEventListener('mouseup', stopDrawing);
colorGrid.addEventListener('mouseleave', stopDrawing);

createColorGrid();

