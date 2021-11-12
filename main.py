from bs4 import BeautifulSoup
import requests

url='https://jsonplaceholder.typicode.com/'
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
# print(soup)
# find by id
# result=soup.find(id="run-message")
# find by class
result=soup.find('code',class_="language-javascript")
print(result.prettify())