import requests
import konlpy as ko
from bs4 import BeautifulSoup
from selenium import webdriver
import re

#selenium for accessing to cgv website
driver = webdriver.Chrome('/Users/LBuser/Desktop/chromedriver.exe')
driver = webdriver.PhantomJS('/Users/LBuser/Desktop/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.implicitly_wait(3)
driver.get('/common/showtimes/iframeTheater.aspx?areacode=01&amp;theatercode=0074')


req = requests.get('http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theaterCode=0074&')

#areacode=01&theaterCode=0074&date=20190104 (왕십리)

html = req.text
CGV_soup = BeautifulSoup(html, 'html.parser')

movie_time = CGV_soup.select('.sect-showtimes .info-timetable li a')
movie_title = CGV_soup.select('.sect-showtimes .info-movie strong')
movie_info = CGV_soup.select('.sect-showtimes .info-hall i li')

# 영화 제목
for title in movie_title:
    title.text

for total in movie_time:
        #print(time)

    print("상영시작시간:", total['data-playstarttime'])
    print("상영지역:", total['data-theatername'])
    print("상영관:", total['data-screenkorname'])
    print("잔여좌석:", total['data-seatremaincnt'])
    print("일자:", total['data-playymd'])
    print("\n")
