import csv
import re
import requests
from typing import Any, Dict, List

class MovieHound:
  def __init__(self, url: str):
    self.url = url
    self.catalog = []

  def fetch(self) -> List[Dict[str, Any]]:
    response = requests.get(self.url)
    data = []
    if response.status_code == 200:
      pattern = re.compile(r'<td class="titleColumn">\s*(\d+)\.\s*<a href="([^"]+)">([^<]+)</a>\s*<span class="secondaryInfo">\((\d{4})\)</span>\s*</td>\s*<td class="ratingColumn.*?><strong>([^<]+)</strong></td>\s*<td class=".*?"><span data-value="([\d,]+)"', re.DOTALL)
      info = pattern.findall(response.text)
      for x in info:
        place, link, title, year, rating, votes = x
        title = title.strip()
        crew = self.getcrew(link)
        data.append({
          "movie_title": title,
          "year": year,
          "place": place,
          "star_cast": crew,
          "rating": rating,
          "vote": self.getvote(votes),
          "link": link,
          "preference_key": int(place) % 4 + 1
        })
    self.catalog = data
    return data

  def getcrew(self, link: str) -> str:
    response = requests.get(f"http://www.imdb.com{link}")
    pattern = re.compile(r'<h4 class="inline">\n(.*?)(?=  See full cast & crew)</div>', re.DOTALL)
    find = pattern.search(response.text)
    if find:
      return find.group(1).strip()
    return ""

  def getvote(self, votes: str) -> int:
    return int(votes.replace(",", ""))

  def tocsv(self, file: str) -> None:
    blocks = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
    with open(file, "w", newline="") as ostream:
      pen = csv.DictWriter(ostream, fieldnames=blocks)
      pen.writeheader()
      for i in self.catalog:
        pen.writerow(i)

if __name__ == '__main__':
  url = 'http://www.imdb.com/chart/top'
  hound = MovieHound(url)
  data = hound.fetch()
  hound.tocsv("movie_results.csv")
