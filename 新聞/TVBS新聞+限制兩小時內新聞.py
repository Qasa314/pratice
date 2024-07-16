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
browser.get("https://news.tvbs.com.tw/realtime")

html_source=browser.page_source  #取得網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
###################時間轉換成電腦格式


df=pd.DataFrame(columns=["時間","分類","標題","網址"])  #宣告空的df

html_source=browser.page_source  #取得網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
area0=soup.find_all("div",class_="list")
area1=area0[9].find_all("li")


for i in range(0,len(area1),1):
    try:
        #print(area1[i].text)
        time1=area1[i].find("div",class_="time").text
        class1=area1[i].find("div",class_="type").text
        title1=area1[i].find("h2",class_="txt").text
        link1=area1[i].find_all("a")[0].get('href')
        if time1=="3小時前":
            break
        print(time1,class1,title1,link1)
    except:
        print("廣告....")

writer=pd.ExcelWriter("tvbs.xlsx", engine = 'xlsxwriter')
df.to_excel(writer,sheet_name="tvbs")
writer.close()

browser.close()
