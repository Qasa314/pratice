import requests
import re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
user_agent = ua.random
headers = {'user-agent': user_agent}

url = "https://mojim.com/twzhot-song.htm"
# 自訂表頭
#headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
html = requests.get(url, headers=headers)  # 將自訂表頭加入 GET 請求中


soup = BeautifulSoup(html.text, 'lxml')

x=soup.find_all("table")
c1=0
for d1 in x[2].find_all("a"):  #列出男生歌曲排行
    c1=c1+1
    if c1%2==1:
        print(d1.text+" https://mojim.com"+d1.get('href'))