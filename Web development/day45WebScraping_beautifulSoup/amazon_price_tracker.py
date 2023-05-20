import requests
from bs4 import BeautifulSoup
import lxml

vacuum_website = "https://www.amazon.com/LG-Batteries-Lightweight-Household-A925KSM/dp/B09ZX8XKZP/ref=sr_1_5?crid=31CO7OG1AOPPY&keywords=vacuum+lg&qid=1680122373&sprefix=vacuum+lg%2Caps%2C83&sr=8-5"
header = {
    'Accept-Language': "en-US,en;q=0.9",
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54"

}
response = requests.get(url = vacuum_website, headers= header)
scraped = response.text
soup = BeautifulSoup(scraped, "html.parser")
price = soup.find("span", class_="a-offscreen").getText()
