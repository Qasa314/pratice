from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions  #2023
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pandas as pd
import xlsxwriter
import time
from datetime import datetime,timedelta
from fake_useragent import UserAgent  #偽裝瀏覽器
import random


#設定瀏覽器驅動程式與爬蟲網址
chrome_options=ChromeOptions()

#設定代理伺服器 
#代理伺服器ip  https://zh.proxyscrape.com/free-proxy-list
proxy_arr=[
    '--proxy-server=http://72.10.164.178:1589',
    ]
proxy=random.choice(proxy_arr)
print("proxy:",proxy)
chrome_options.add_argument(proxy)

#偽裝瀏覽器
ua=UserAgent()
a=ua.random
user_agent=ua.random
print("user_agent:",user_agent)
chrome_options.add_argument(f'user-agent={user_agent}')

chrome_options.add_experimental_option("detach",True)
browser=webdriver.Chrome(options=chrome_options)
browser.get("https://mojim.com/twzhot-song.htm")
time.sleep(5)



'''
#捲動瀏覽器(使用鍵盤向下按鈕)
actions=ActionChains(browser)
elem=browser.find_element(By.CLASS_NAME,"btnApply")
actions.move_to_element(elem).perform()  #移動到物件上
time.sleep(2)
for j in range(0,500,1):
    elem.send_keys(Keys.ARROW_DOWN) #鍵盤向下按鈕
    time.sleep(0.1)
'''



#宣告變數值
df=pd.DataFrame(columns=["曲名","歌手","網址"])  #宣告空的df



#爬大區塊
html_source=browser.page_source  #取得網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
area0=soup.find_all("div",id="mx5_A")   #男生排行榜
#print(area0[0].text)
area1=area0[0].find_all("tr") #每首歌的區塊


#爬細節
for i in range(1,len(area1)-1,1):
    area2=area1[i].find_all("a")
    song1=area2[0].text
    name1=area2[1].text
    link1="https://mojim.com"+area2[0].get('href')
    #if i>100:break
    print("曲名:",song1)
    print("歌手:",name1)
    print("網址:",link1)
    print("------------------")    
    df.loc[i]=[song1,name1,link1]  #紀錄存到pandas


browser.close()


#儲存成檔案
#df.to_csv("songs.csv",encoding="utf_8_sig")  #存成csv
#存成excel
writer=pd.ExcelWriter("songs.xlsx", engine = 'xlsxwriter')
df.to_excel(writer,sheet_name="songs")
writer.close()
