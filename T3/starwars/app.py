import os
from bl.sw_service import *
from flask import Flask, jsonify

print("Application startup")
port = int(os.environ['PORT'])
print("PORT::", port)

app = Flask(__name__)

url = "https://swapi.dev/api/films/"

@app.route("/", methods=['GET'])
def list_movies():
    return fetchmovies(source=url)

@app.route("/cast", methods=['GET'])
def list_characters():
    return fetchcast(source=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)
