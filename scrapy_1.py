import requests
from bs4 import BeautifulSoup

url = "http://scrapying-study.firebaseapp.com/01"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

soup.find("p")
soup.find_all("p")
soup.find_all("p", limit=2)

soup.find("th","tablehead")
soup.find("th",class_="tablehead")
soup.find("th",attrs = {"class":"tablehead"})
soup.find("h1",attrs = {"title":"welcome"})
soup.find(id="hello")
