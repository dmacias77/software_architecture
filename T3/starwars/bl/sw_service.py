import requests

dataurl = "https://swapi.dev/api/films/"

def fetch_movies():
	data = requests.get(dataurl).json()

	movies = []
	for i in data["results"]:
		charurl = i["characters"]

		cast = []
		for j in charurl:
			data = requests.get(j).json()
			cast.append(data["name"])
		movies.append({
			"id": i["episode_id"],
			"name": i["title"],
			"characters": cast
		})
	return movies
