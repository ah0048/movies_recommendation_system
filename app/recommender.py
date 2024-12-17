import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, dataset_path):
        # Load dataset
        self.dataset = pd.read_csv(dataset_path)
        self.vectorizer = None
        self.similarity_matrix = None

    def preprocess_data(self):
        # Select relevant columns and fill missing values
        for col in ['genres', 'keywords', 'overview', 'tagline', 'vote_average']:
            self.dataset[col] = self.dataset[col].fillna('')

        # Combine relevant features into a single string
        self.dataset['combined_features'] = (
            self.dataset['genres'] + " " +
            self.dataset['keywords'] + " " +
            self.dataset['overview'] + " " +
            self.dataset['tagline'] + " " +
            str(self.dataset['vote_average'])
        )

    def calculate_similarity(self):
        # Vectorize the combined features using TF-IDF
        self.vectorizer = TfidfVectorizer(stop_words='english')
        feature_matrix = self.vectorizer.fit_transform(self.dataset['combined_features'])

        # Calculate cosine similarity
        self.similarity_matrix = cosine_similarity(feature_matrix)

    def recommend(self, movie_title, top_n=5):
        # Check if the movie exists in the dataset
        if movie_title not in self.dataset['title'].values:
            return []

        # Get the index of the selected movie
        movie_index = self.dataset[self.dataset['title'] == movie_title].index[0]

        # Get similarity scores for the movie
        similarity_scores = list(enumerate(self.similarity_matrix[movie_index]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

        # Extract top N recommendations (excluding the selected movie itself)
        top_movies = [self.dataset.iloc[i[0]]['title'] for i in similarity_scores[1:top_n + 1]]
        return top_movies
