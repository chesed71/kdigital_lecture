
import requests
from bs4 import BeautifulSoup

url = 'https://scrapying-study.firebaseapp.com/01/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

result = []
headers = soup.find_all("th")
keys = []
for th in headers:
    keys.append(th.text)

tbody = soup.find("tbody")
tr_list = tbody.find_all("tr")
for tr in tr_list:
    td_list = tr.find_all("td")
    values = []
    for td in td_list:
        values.append(td.text)
    
    result.append(dict(zip(keys, values)))

print(result)