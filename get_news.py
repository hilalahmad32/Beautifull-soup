from bs4 import BeautifulSoup
import requests
import time

def find():
    url="https://www.geo.tv/latest-news"
    html_text=requests.get(url)

    soup=BeautifulSoup(html_text.text,"lxml")
    news=soup.find_all('div',class_='col-xs-6 col-sm-6 col-lg-6 col-md-6 singleBlock')

    for index,content in enumerate(news):
        news_time=content.find('span').text
        if 'minutes' in news_time:
            news_heading=content.find('h2').text
            detail=content.li.a['href']
            time.sleep(1)
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f'heading : {news_heading} \n')
                f.write(f'posted time :{news_time} \n')
                f.write(f'Info Link :{detail} \n')
                print(f'File is Saved : {index}')
            print('')

if __name__ == '__main__':
    while True:
        find()
        time.sleep(4)
        print("Program well start in 4 second")