import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

class MovieRecommender:
    def __init__(self, data_path="movies.csv"):
        print("Initializing Machine Learning Recommender Engine...")
        
        # Load dataset
        self.movies_df = pd.read_csv(data_path)
        
        # The key to content-based filtering is combining relevant features into a single pool of words.
        # We will use 'genre' and 'tags' to create a comprehensive 'features' column for NLP to process.
        self.movies_df['features'] = self.movies_df['genre'] + " " + self.movies_df['tags']
        
        # Initialize Term Frequency-Inverse Document Frequency (TF-IDF) Vectorizer
        # This translates our English textual metadata into a mathematical vector space
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.feature_vectors = self.vectorizer.fit_transform(self.movies_df['features'])
        
        # Calculate the pure mathematical cosine similarity distance between all movies
        self.similarity_score = cosine_similarity(self.feature_vectors)
        print("Engine initialized successfully.")

    def get_recommendations(self, movie_name, top_n=5):
        """
        Takes a movie title string, finds the closest match in the database,
        and uses the NLP Cosine Similarity matrix to return the top N recommendations.
        """
        # Create list of all titles for fuzzy matching
        list_of_all_titles = self.movies_df['title'].tolist()
        
        # Use diff-lib to find the closest match in case of minor typos (e.g. 'Avenger' -> 'Avengers: Endgame')
        find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles, n=1, cutoff=0.4)
        
        if not find_close_match:
            return {"error": f"Sorry! We couldn't find a close match for '{movie_name}' in our database."}
        
        close_match = find_close_match[0]
        
        # Find the mathematical index of the matched movie
        movie_index = self.movies_df[self.movies_df['title'] == close_match].index[0]
        
        # Get a list of similarity scores exclusively for this specific movie against all others
        similarity_list = list(enumerate(self.similarity_score[movie_index]))
        
        # Sort them by the highest score (excluding the movie itself which is 1.0)
        sorted_similar_movies = sorted(similarity_list, key=lambda x: x[1], reverse=True)[1:top_n+1]
        
        # Generate the payload list
        recommendations = []
        for index, _ in sorted_similar_movies:
            title = self.movies_df.iloc[index]['title']
            genre = self.movies_df.iloc[index]['genre']
            recommendations.append({"title": title, "genre": genre})
            
        return {
            "matched_movie": close_match,
            "recommendations": recommendations
        }

# Manual debugging entry point
if __name__ == "__main__":
    ai = MovieRecommender()
    print(ai.get_recommendations("Matrix"))
