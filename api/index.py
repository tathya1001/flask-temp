# /api/index.py

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify("{Flask Vercel Example - Hello World}")


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404



if __name__ == '__main__':
    app.run(debug=True)
