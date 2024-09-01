import os
import pickle
import requests
from flask import Flask, jsonify, abort
from flask_cors import CORS
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)  
load_dotenv()


# file_path = os.path.join(os.path.dirname(__file__), 'reduced_movies.pkl')
# with open(file_path, 'rb') as f:
#     reduced_data = pickle.load(f)

@app.route("/recommend/<string:movie>")
def recommend(movie):

    return jsonify(["hello", "hi"])

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": e.description}), 404

if __name__ == '__main__':
    app.run(debug=True)
