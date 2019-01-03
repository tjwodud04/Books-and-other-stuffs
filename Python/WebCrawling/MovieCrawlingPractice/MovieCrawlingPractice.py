import requests
import konlpy as ko
from bs4 import BeautifulSoup
from selenium import webdriver


# driver = webdriver.Chrome('/Users/J/Desktop/chromedriver.exe')
# driver = webdriver.PhantomJS('/Users/J/Desktop/phantomjs-2.1.1-windows/bin/phantomjs.exe')
# driver.implicitly_wait(3)
# driver.get('/common/showtimes/iframeTheater.aspx?areacode=01&amp;theatercode=0074')

default_cgv = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?'

#areacode=01&theaterCode=0074&date=20190104 (왕십리)
area = 'areacode=01&'
theater = 'theaterCode=0074&'
date = 'date=20190104'

CGVTime_html = requests.get(default_cgv + area + theater + date).text
CGVTime_soup = BeautifulSoup(CGVTime_html, 'html.parser')

movie_info = CGVTime_soup.select(".sect-showtimes .info-movie")
movie_title = CGVTime_soup.select(".sect-showtimes .info-movie strong")

# 영화 제목
# for info in movie_info:
#     print(info.text)

#for title in movie_title:
#   print(title.text)

movie_time = CGVTime_soup.select(".sect-showtimes .info-timetable li a")
movie_schedule = CGVTime_soup.select(".sect-schedule .item-wrap span strong")

for title in movie_title:
    for schedule in movie_schedule:
        print(title.text + schedule.text)

for time in movie_time:
    #print(time)

    print("영화제목:", )
    print("상영시간:", time['data-playstarttime'])
    print("상영관:", time['data-screenkorname'])
    print("잔여좌석:", time['data-seatremaincnt'])
    print("일자:", time['data-playymd'])
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