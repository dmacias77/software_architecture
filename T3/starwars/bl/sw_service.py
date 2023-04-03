#starwars_service file
from flask import jsonify, request
import requests

dataurl = "https://swapi.dev/api/films/"

def fetchcast(source: str):
    data = requests.get(source).json()
    mid = request.args.get('episode_id', default=-1, type=int)
    cast = []
    if mid != -1:
        for i in data["results"]:
            if i["episode_id"] == mid:
                cast.extend(i["characters"])
    else:
        for i in data["results"]:
            cast.extend(i["characters"])
    characters = []
    for i in cast[0]:
        data = requests.get(i).json()
        name = data['name']
        characters.append(name)
    return jsonify(characters)

def fetchmovies(source: str):
    data = requests.get(source).json()

    movies_temp = []
    for i in data["results"]:
        movie = {"id": i["episode_id"], "name": i["title"]}
        movies_temp.append(movie)
    movies = sorted(movies_temp, key=lambda movie: movie['id'])

    return jsonify(movies)
