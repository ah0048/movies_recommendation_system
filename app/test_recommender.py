from recommender import Recommender

# Path to dataset
dataset_path = "data/tmdb_dataset.csv"

# Instantiate and test the recommender system
recommender = Recommender(dataset_path)

# Preprocess the data and calculate similarity
recommender.preprocess_data()
recommender.calculate_similarity()

# Test recommendations
movie_title = "The Godfather"  # Replace with a movie title from the dataset
recommendations = recommender.recommend(movie_title, top_n=5)

print(f"Recommendations for '{movie_title}':")
print(recommendations)
