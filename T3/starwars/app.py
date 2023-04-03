import os
from bl.sw_service import fetch_movies
from flask import Flask

from flask import jsonify

print("Application startup")
port = int(os.environ['PORT'])
print("PORT::", port)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def list_movies():
    movies = fetch_movies()
    return jsonify(movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)
