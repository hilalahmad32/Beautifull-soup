from bs4 import BeautifulSoup
import requests
import time

url="https://www.geo.tv/"
content= requests.get(url)

# print(content)
soup=BeautifulSoup(content.text,"html.parser")
# print(soup.prettify())
# result=soup.find_all("div")
result=soup.find_all("h2")

for title_tag in result:
    title_name=title_tag.text
    time.sleep(1)
    print(title_name)
