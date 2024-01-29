import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movie_data = response.text

soup = BeautifulSoup(movie_data, "html.parser")
greatest_movies = soup.findAll("h3", class_="title")

with open("movie.txt", "w") as movie_file:
    for movie in greatest_movies[::-1]:
        data = movie.getText()
        movie_file.write(data + "\n")





