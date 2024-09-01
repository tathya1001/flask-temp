import os
import pickle
import requests
from flask import Flask, jsonify, abort
from flask_cors import CORS
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)  # Enable CORS if you're calling this API from a frontend application

# Load environment variables from a .env file
load_dotenv()

# Load API key from environment variable
TMDB_API_KEY = os.getenv('TMDB_API_KEY')

# Check if the API key is loaded
if not TMDB_API_KEY:
    raise ValueError("TMDB API key not found in environment variables.")

# Load the .pkl file relative to the current file's directory
file_path = os.path.join(os.path.dirname(__file__), 'reduced_movies.pkl')
with open(file_path, 'rb') as f:
    reduced_data = pickle.load(f)

def get_poster_path(movie_id, api_key):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return None

@app.route("/recommend/<string:movie>")
def recommend(movie):
    # movie_data = reduced_data[movie.title()]

    # if not movie_data:
    #     return abort(404, description="Movie not found")

    # recommended_movies_posters = []
    
    # for recommended_movie in movie_data['recommendations']:
    #     poster_url = get_poster_path(recommended_movie['movie_id'], TMDB_API_KEY)
    #     if poster_url:
    #         recommended_movies_posters.append({
    #             "title": recommended_movie.get('title'),
    #             "poster_url": poster_url
    #         })
    
    # if not recommended_movies_posters:
    #     return jsonify({"message": "No recommendations found"}), 404

    return jsonify(reduced_data[0])

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": e.description}), 404

if __name__ == '__main__':
    app.run(debug=True)
