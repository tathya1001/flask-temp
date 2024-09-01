from flask import Flask, jsonify
import pickle

app = Flask(__name__)
# reduced_data = pickle.load(open('reduced_movies.pkl', 'rb'))

@app.route("/")
def home():
    return jsonify({"hello"})


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404



if __name__ == '__main__':
    app.run(debug=True)
