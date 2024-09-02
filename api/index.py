from flask import Flask, jsonify
from flask_cors import CORS
import os
import pickle

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the .pkl file relative to the current file's directory
file_path = os.path.join(os.path.dirname(__file__), 'reduced_movies.pkl')
with open(file_path, 'rb') as f:
    reduced_data = pickle.load(f)

@app.route("/recommend/<string:movie>", methods=['GET'])
def home(movie):
    data = {}
    for i in reduced_data:
        if i['title'] == movie:
            data = i
            break
    return jsonify(data)

@app.route("/test", methods=['GET'])
def test():
    return jsonify(['hello', 'hi'])


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
