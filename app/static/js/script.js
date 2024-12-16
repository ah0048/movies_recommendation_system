const API_BASE = "http://127.0.0.1:5000";

// Populate the dropdown with movie titles
async function fetchMovies() {
    const response = await fetch(`${API_BASE}/movies`);
    const movies = await response.json();
    const dropdown = document.getElementById("movieTitle");

    movies.forEach((movie) => {
        const option = document.createElement("option");
        option.value = movie;
        option.textContent = movie;
        dropdown.appendChild(option);
    });
}

// Fetch recommendations on form submission
document.getElementById("recommenderForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    const movieTitle = document.getElementById("movieTitle").value;

    const response = await fetch(`${API_BASE}/recommend`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ movie_title: movieTitle }),
    });

    const recommendations = await response.json();
    const recommendationsList = document.getElementById("recommendations");
    recommendationsList.innerHTML = ""; // Clear previous recommendations

    recommendations.forEach((movie) => {
        const li = document.createElement("li");
        li.textContent = movie;
        li.classList.add("list-group-item");
        recommendationsList.appendChild(li);
    });
});

// Initialize the page
fetchMovies();
