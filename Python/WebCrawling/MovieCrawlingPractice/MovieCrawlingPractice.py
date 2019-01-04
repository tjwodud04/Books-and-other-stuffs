import requests
import konlpy as ko
from bs4 import BeautifulSoup
from selenium import webdriver
import re

# driver = webdriver.Chrome('/Users/LBuser/Desktop/chromedriver.exe')
# driver = webdriver.PhantomJS('/Users/LBuser/Desktop/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
# driver.implicitly_wait(3)
# driver.get('/common/showtimes/iframeTheater.aspx?areacode=01&amp;theatercode=0074')

# requests = requests.get('http://www.cgv.co.kr/reserve/show-times/?areacode=01&theaterCode=0074&date=20190103')
# contents = requests.content
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# #print(soup)
#
# body = soup.find("body")
#
# print(soup)
# #li = soup.find
# # contents = soup.select(
# #     'li > div'
# # )
# # print(soup)
# # for contentinfo in contents:
# #     print(contentinfo)

req = requests.get('http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theaterCode=0074&')

#areacode=01&theaterCode=0074&date=20190104 (왕십리)

html = req.text
CGV_soup = BeautifulSoup(html, 'html.parser')

movie_time = CGV_soup.select('.sect-showtimes .info-timetable li a')
movie_title = CGV_soup.select('.sect-showtimes .info-movie strong')
movie_info = CGV_soup.select('.sect-showtimes .info-hall i li')

print(movie_title)

# 영화 제목
for title in movie_title:
    title.text

#titlelist = movie_title.split()

#print(titlelist)
#titlelist.strip('\n')

#print(titlelist)

for total in movie_time:
        #print(time)

    print("상영시작시간:", total['data-playstarttime'])
    print("상영지역:", total['data-theatername'])
    print("상영관:", total['data-screenkorname'])
    print("잔여좌석:", total['data-seatremaincnt'])
    print("일자:", total['data-playymd'])
    print("\n")

# requests = requests.get('http://www.cgv.co.kr/reserve/show-times/?areacode=01&theaterCode=0074&date=20190103')
# contents = requests.content
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# #print(soup)
#
# body = soup.find("body")
#
# print(soup)
# #li = soup.find
# # contents = soup.select(
# #     'li > div'
# # )
# # print(soup)
# # for contentinfo in contents:
# #     print(contentinfo)