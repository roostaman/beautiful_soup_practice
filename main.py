import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
top_movies_web = response.text

soup = BeautifulSoup(top_movies_web, "html.parser")

titles = soup.find_all(name="h3", class_="title")

titles_text = [title.get_text() for title in titles]
titles_text.reverse()

with open(file="movies.txt", mode="w") as file:
    for text in titles_text:
        file.write(text + "\n")
