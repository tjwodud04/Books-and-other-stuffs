"""
https://beomi.github.io/2017/04/20/HowToMakeWebCrawler-Notice-with-Telegram/
http://www.cgv.co.kr/reserve/show-times/?areacode=01&theaterCode=0074&date=20190205
https://cpuu.postype.com/post/26176
https://iamaman.tistory.com/1692
https://medium.com/bothub-studio-ko/
%EC%B1%97%EB%B4%87-%EB%A7%8C%EB%93%A4%EA%B8%B0-%EC%98%81%ED%99%94-%EC%83%81%EC%98%81%EA%B4%80-%EC%B0%BE%EA%B8%B0-ec9bbff353d8
"""

import requests
from bs4 import BeautifulSoup
import os
import telegram
import time
import re

bot = telegram.Bot(token = '')
chat_id = bot.getUpdates()[-1].message.chat.id


BASE_DIR = os.path.dirname(os.path.abspath('C:/Users/J/Desktop'))

req = requests.get('http://www.cgv.co.kr/reserve/show-times/?areacode=01&theaterCode=0074&date=20190205')
req.encoding = 'utf-8'

html = req.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.findAll('div.sect-showtimes')

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('\n', data)

removedposts = remove_html_tags(str(posts))

with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_read:
    before = f_read.readline()
    f_read.close()
    if before != posts:
        bot.sendMessage(chat_id=chat_id, text='영화 상영시간표 업데이트')
        bot.sendMessage(chat_id=chat_id, text='http://www.cgv.co.kr/reserve/show-times/?areacode=01&theaterCode=0074&date=20190205')
        with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
            f_write.write(removedposts)
            f_write.close()
