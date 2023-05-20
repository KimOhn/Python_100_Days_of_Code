import requests
from bs4 import BeautifulSoup
import pprint
date = "2003-09-01"
billboard_website = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url = billboard_website)
content = response.text

soup = BeautifulSoup(content, 'html.parser')
titles = soup.select(selector = "li ul li h3")
hit100 = [tag.getText().strip() for tag in titles]

print(hit100)
