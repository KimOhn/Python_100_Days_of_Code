from bs4 import BeautifulSoup
import requests

response = requests.get(url = "https://news.ycombinator.com/")
yc_content = response.text
soup = BeautifulSoup(yc_content, 'html.parser')
all_span_title  = soup.find_all(name = "span", class_="titleline")

titles = []
links = []
for tag in all_span_title:
    anchor_tag = tag.findNext("a")
    title = anchor_tag.getText()
    link = anchor_tag.get("href")
    titles.append(title)
    links.append(link)

all_span_score =  soup.find_all(name = "span", class_="score")

scores = [int(tag.getText().split()[0]) for tag in all_span_score]

most_popular_index = scores.index(max(scores))

print(titles[most_popular_index])
print(links[most_popular_index])
