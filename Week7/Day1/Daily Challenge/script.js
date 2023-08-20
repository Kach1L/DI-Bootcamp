// Planets array
const planets = [
    { name: "Mercury", color: "gray", moons: 0 },
    { name: "Venus", color: "orange", moons: 0 },
    { name: "Earth", color: "blue", moons: 1 },
    { name: "Mars", color: "red", moons: 2 },
    { name: "Jupiter", color: "tan", moons: 79 },
    { name: "Saturn", color: "yellow", moons: 83 },
    { name: "Uranus", color: "lightblue", moons: 27 },
    { name: "Neptune", color: "darkblue", moons: 14 }
];

// Get the section where planets will be displayed
const listPlanetsSection = document.querySelector('.listPlanets');

// Loop through the planets array and render each planet and its moons
planets.forEach(planet => {
    const planetDiv = document.createElement('div');
    planetDiv.className = 'planet ' + planet.name.toLowerCase();
    planetDiv.style.backgroundColor = planet.color;

    const planetName = document.createElement('p');
    planetName.textContent = planet.name;

    planetDiv.appendChild(planetName);
    listPlanetsSection.appendChild(planetDiv);

    // Create moons for the planet
    for (let i = 0; i < planet.moons; i++) {
        const moonDiv = document.createElement('div');
        moonDiv.className = 'moon';
        moonDiv.style.left = Math.random() * 60 + 'px'; // Spread moons randomly around the planet
        moonDiv.style.top = Math.random() * 60 + 'px';
        planetDiv.appendChild(moonDiv);
    }
});
