from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
films_webpage = response.text
soup = BeautifulSoup(films_webpage, "html.parser")

films = soup.find_all(name="h3", class_="title")

films_list = []

for film in films:
    films_list.append(film.getText())

films_list.reverse()
print(films_list)

file = open("100films.txt", "w")
for film in films_list:
    file.write(f"{film}\n")
file.close()
