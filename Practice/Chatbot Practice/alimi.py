# 참고
# https://m.blog.naver.com/PostView.nhn?blogId=potter777777&logNo=220692034035&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F
# https://rrbb014.tistory.com/28

from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/J/Desktop/chromedriver.exe')

driver.get('http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0074&date=20190425')
#driver.switch_to.frame("viewport")

#driver.find_element_by_xpath("//ul [class=item]").click()
req = driver.page_source
soup = BeautifulSoup(req,'html.parser')
information_list = soup.find_all('item')
print(information_list)