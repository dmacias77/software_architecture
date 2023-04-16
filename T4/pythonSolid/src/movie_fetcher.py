import csv
import re
import requests
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

class WebHound(ABC):
    @abstractmethod
    def getmovies(self):
        pass

class DataHound(WebHound):
    def __init__(self, url):
        self.url = url

    def getmovies(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'lxml')
        movies = soup.select('td.titleColumn')
        links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
        crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
        ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
        votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]
        catalog = []
        for index in range(0, len(movies)):
            movie_string = movies[index].get_text()
            movie = (' '.join(movie_string.split()).replace('.', ''))
            movie_title = movie[len(str(index)) + 1:-7]
            year = re.search('\((.*?)\)', movie_string).group(1)
            place = movie[:len(str(index)) - (len(movie))]
            data = {"movie_title": movie_title,
                    "year": year,
                    "place": place,
                    "star_cast": crew[index],
                    "rating": ratings[index],
                    "vote": votes[index],
                    "link": links[index],
                    "preference_key": index % 4 + 1}
            catalog.append(data)
        return catalog

class CSV(ABC):
    @abstractmethod
    def to_csv(self, movie_list):
        pass

class CSVEditor(CSV):
    def __init__(self, filename, fields):
        self.filename = filename
        self.fields = fields

    def to_csv(self, movie_list):
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            for movie in movie_list:
                writer.writerow({**movie})

def main():
    url = 'http://www.imdb.com/chart/top'
    hound = DataHound(url)
    catalog = hound.getmovies()
    col = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
    editor = CSVEditor("movie_results.csv", col)
    editor.to_csv(catalog)


if __name__ == '__main__':
    main()
