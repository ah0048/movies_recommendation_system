# Movie Recommendation System

## Overview

This is a content-based movie recommendation system that allows users to select a movie and receive a list of similar movies. The system is built using Python for the backend and a simple HTML/CSS + JavaScript frontend for the user interface.

The recommendations are generated using cosine similarity on movie features such as genres, keywords, and titles.

## Features

- Fetch a list of movies dynamically from the backend API.
- Recommend top 5 similar movies based on a selected movie.
- Simple and responsive user interface.
- Clean API endpoints for backend processing.

## Project Structure

```bash
movies_recommendation_system/
├── README.md
├── app/
│   ├── __init__.py
│   ├── main.py              # Flask app with API routes
│   ├── recommender.py       # Recommender logic and data processing
│   ├── utils.py             # Helper functions
│   ├── static/
│   │   └── css/
│   │       └── style.css    # Basic styling for the frontend
│   ├── templates/
│   │   ├── index.html       # Frontend HTML file
│   │   └── script.js        # JavaScript for frontend interactivity
│   └── test_recommender.py  # Test cases for the recommender logic
├── data/
│   └── tmdb_dataset.csv     # Dataset containing movie information
├── requirements.txt         # Project dependencies
└── run.py                   # Entry point to run the app
```
## Tech Stack
## Backend

Python (Flask) for API development.

Pandas for data processing and manipulation.

Cosine Similarity (from scikit-learn) for calculating movie similarity.

Frontend

HTML/CSS for structure and styling.

Bootstrap for responsive design.

JavaScript for fetching data and updating the UI dynamically.

Setup Instructions
Follow these steps to run the project locally:

1. Clone the Repository
```bash
git clone https://github.com/ah0048/movies_recommendation_system
cd movies_recommendation_system
```
2. Set Up the Environment
Ensure you have Python 3.8+ installed. Create a virtual environment and install the dependencies:

# Create a virtual environment
```bash
python3 -m venv venv
```
# Activate the virtual environment
```bash
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```

# Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the Application
Start the Flask server:

```bash
cd app
python3 main.py
```
The application will run on http://127.0.0.1:5000.

## API Endpoints
Endpoint	Method	   Description
/movies	    GET	       Fetches the list of movie titles.
/recommend	POST	   Returns 5 recommendations for a movie.
Example Request for /recommend
Request:

```bash
POST /recommend
Content-Type: application/json

{
    "movie_title": "The Matrix"
}
```
Response:

```bash
[
    "The Matrix Reloaded",
    "The Matrix Revolutions",
    "Inception",
    "Blade Runner",
    "The Terminator"
]
```
## How It Works
## Preprocessing
The dataset is loaded from data/tmdb_dataset.csv.

Features such as genres, keywords, and titles are combined into a single column for similarity calculations.

## Similarity Calculation
TF-IDF Vectorization is applied to the combined features to convert them into numerical vectors.

Cosine Similarity is calculated between all movie vectors to measure their similarity.

## Frontend Interaction
The frontend fetches movie titles to populate the dropdown list.

On selecting a movie and clicking "Get Recommendations," it sends a POST request to the /recommend endpoint.

The response is displayed as a list of recommended movies.

## Future Improvements
Add collaborative filtering for user-based recommendations.

Implement deployment on Heroku or AWS.

Enhance the frontend with better UI/UX design.

## Acknowledgments
TMDB Dataset: The dataset used for movie recommendations.

Flask: For building the backend API.

Bootstrap: For frontend styling.
