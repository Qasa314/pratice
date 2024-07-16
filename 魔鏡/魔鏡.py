import requests
from bs4 import BeautifulSoup
url="https://mojim.com/twznew.htm"
html=requests.get(url)  #連線抓網頁
html.encoding="UTF-8"   #強制編碼
c=""
sp=BeautifulSoup(html.text,'lxml')

area1=sp.find_all("dl",class_="ha0")
area2=area1[0].find_all("h1")
for i in area2:
    c=c+i.text.split("\n")[0]+","+i.text.split("\n")[1].split(" ")[0]+","+i.text.split("\n")[2]+"\n"
    print(c)
file=open("歌詞.csv","w+",encoding="UTF-8-SIG")
file.write(str(c))
file.close()