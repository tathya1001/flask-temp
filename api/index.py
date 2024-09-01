from flask import Flask, jsonify
import os
import pickle

app = Flask(__name__)

# Load the .pkl file relative to the current file's directory
file_path = os.path.join(os.path.dirname(__file__), 'reduced_movies.pkl')
with open(file_path, 'rb') as f:
    reduced_data = pickle.load(f)

@app.route("/")
def home():
    return jsonify(reduced_data[0])

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
