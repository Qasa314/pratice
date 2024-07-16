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
import requests



#設定瀏覽器驅動程式與爬蟲網址
chrome_options=ChromeOptions()
chrome_options.add_experimental_option("detach",True)
browser=webdriver.Chrome(options=chrome_options)

urls=["https://stat.motc.gov.tw/mocdb/stmain.jsp?sys=220&ym=11101&ymt=11210&kind=21&type=1&funid=b710201&cycle=1&outmode=0&compmode=0&outkind=1&fldspc=0,28,&rdm=dblbddcl"]
urlnames=["旅遊數據"]


#存成excel
writer=pd.ExcelWriter("travel.xlsx", engine = 'xlsxwriter') #開新檔案

for p in range(0,1,1):
    browser.get(urls[p])
    time.sleep(2)
    #browser.refresh() #重新整理
    #time.sleep(3)

    #爬欄位名稱
    html_source=browser.page_source  #取得網頁原始碼
    soup=BeautifulSoup(html_source,"lxml")
    area0=soup.find_all("table")   #統計表大區塊
    #print(area0[1].text)
    
    area1=area0[1].find_all("tr")	#第一個統計表所有列
    thead1=area1[0].find_all("th") #數據標題
    #print(thead1[1].text)    
    c=[]
    for i in thead1:
        c.append(i.text)

    #宣告變數值
    df=pd.DataFrame(columns=c)  #宣告空的df
    #print(df)
  
    #爬數據
    for k in range(1,len(area1),1):
        s=[]
        month1=area1[k].find("th").text
        s.append(month1)
        data1=area1[k].find_all("td")
        for j in data1:
            s.append(j.text)
        df.loc[k]=s  #紀錄存到pandas

    print(df)
    
    #儲存成檔案
    #df.to_csv("cpbl.csv",encoding="utf_8_sig")  #存成csv
    df.to_excel(writer,sheet_name=urlnames[p])
    
    
writer.close()   #關閉檔案
browser.close()


