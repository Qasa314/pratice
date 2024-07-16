from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions  #202
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pandas as pd
import xlsxwriter
import time
from datetime import datetime,timedelta
import requests


chrome_options=ChromeOptions()
chrome_options.add_experimental_option("detach",True)
browser=webdriver.Chrome(options=chrome_options)
browser.get("https://www.ettoday.net/news/news-list.htm")

html_source=browser.page_source  #取得網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
###################時間轉換成電腦格式
now1=datetime.now()#現在時間
two_hours=timedelta(hours=2)#兩小時
two_hours_ago=now1-two_hours
two_hours_ago_time=two_hours_ago.strftime("%Y/%m/%d %H:%M")  #將時間格式轉換成東森新聞雲的時間格式

df=pd.DataFrame(columns=["時間","分類","標題","網址"])  #宣告空的df

html_source=browser.page_source  #取得網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
area0=soup.find("div",class_="part_list_2")
area1=area0.find_all("h3")
for i in range(4,len(area1),1):
        #print(area1[i].text)
        time1=area1[i].find("span",class_="date").text
        class1=area1[i].find("em").text
        title1=area1[i].find("a").text
        link1=area1[i].find("a").get('href')
#####################################時間比大小################################
        if time1 >= two_hours_ago_time :
            print(time1,class1,title1,link1)#大的輸出
        
            print("-------------------")    
            df.loc[i]=[time1,class1,title1,link1]
        else:
            break#小的就斷掉
writer=pd.ExcelWriter("ds.xlsx", engine = 'xlsxwriter')
df.to_excel(writer,sheet_name="ds")
writer.close()

browser.close()