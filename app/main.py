from flask import Flask, request, jsonify, render_template
from recommender import Recommender

app = Flask(__name__)

# Path to your dataset
dataset_path = "../data/tmdb_dataset.csv"

# Initialize the recommender
recommender = Recommender(dataset_path)
recommender.preprocess_data()
recommender.calculate_similarity()

@app.route('/')
def home():
    """Serve the main HTML page."""
    return render_template('index.html')

@app.route('/movies', methods=['GET'])
def get_movies():
    """Fetch the list of movie titles."""
    titles = recommender.dataset['title'].tolist()
    return jsonify(titles)

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    """Fetch recommendations for a given movie."""
    data = request.get_json()
    movie_title = data.get('movie_title', '')
    recommendations = recommender.recommend(movie_title, top_n=5)
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
