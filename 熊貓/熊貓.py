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
browser=webdriver.Chrome()
browser.get("https://www.foodpanda.com.tw/city/taipei-city")
time.sleep(10)
html_source=browser.page_source  #取得網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
area1=soup.find_all("div",class_="bds-c-grid-item vendor webfound-refresh")
df=pd.DataFrame(columns=["名稱","星數","網址"])

for i in range(0,len(area1),1):
    name1=area1[i].find("div",class_="vendor-name f-title-small-font-size fw-title-small-font-weight lh-title-small-line-height ff-title-small-font-family ffs-title-small-font-feature-settings").text
    link1=area1[i].find("a")["href"]
    try:
        star1=area1[i].find("span",class_="bds-c-rating__label-primary f-label-small-font-size fw-label-small-font-weight lh-label-small-line-height ff-label-small-font-family").text
    except:
        star1=""
    print(name1,star1)
    df.loc[i]=[name1,star1,link1]




writer=pd.ExcelWriter("熊貓.xlsx", engine = 'xlsxwriter')
df.to_excel(writer,sheet_name="熊貓")
writer.close()

browser.close()
