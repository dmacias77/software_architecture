#starwars_service file
from flask import jsonify, request
import json
import requests

dataurl = "https://swapi.dev/api/films/"

def fetchcast(source: str):
    data = requests.get(source).json()
    mid = request.args.get('episode_id', default=-1, type=int)

    sources = []
    if mid != -1:
        for i in data["results"]:
            if i["episode_id"] == mid:
                sources.extend(i["characters"])
    else:
        for i in data["results"]:
            sources.extend(i["characters"])

    # La línea debajo se la pedí a ChatGPT (y le pedí que me la explicara).
    url_list = list(set([x for x in sources if sources.count(x) > 1]))
    # Lo remarco para que no provoque sospechas de copia.

    cast = []
    for i in url_list:
        url_info = requests.get(i).json()
        name = url_info["name"]
        cast.append(name)

    return jsonify(cast)

def fetchmovies(source: str):
    data = requests.get(source).json()

    movies_temp = []
    for i in data["results"]:
        movie = {"id": i["episode_id"], "name": i["title"]}
        movies_temp.append(movie)
    movies = sorted(movies_temp, key=lambda movie: movie['id'])

    return jsonify(movies)
