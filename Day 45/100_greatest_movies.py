from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")

movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movies.reverse()
print(movies)

with open('movies.txt', 'w', encoding='utf-8') as file:
    for movie in movies:
        file.write(movie + "\n")
