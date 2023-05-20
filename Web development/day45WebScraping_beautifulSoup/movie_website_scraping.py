import requests
from bs4 import BeautifulSoup
import pandas
movie_website = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url = movie_website)
content = response.text
soup = BeautifulSoup(content, "html.parser")

all_h3_tags = soup.find_all(name = "h3", class_="title")

movie_titles = [tag.getText() for tag in all_h3_tags]
movies = movie_titles[::-1]
movie_df = pandas.DataFrame(movies)

movie_df.to_csv("movies_to_watch.csv", index=False, header = None)