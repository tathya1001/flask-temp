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

@app.route("/recommend/<string:movie>")
def recommend(movie):

    return jsonify(reduced_data[0])

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": e.description}), 404

if __name__ == '__main__':
    app.run(debug=True)
