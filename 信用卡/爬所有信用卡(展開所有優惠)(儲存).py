from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions  #2023改版
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pandas as pd
import xlsxwriter
import time
from datetime import datetime,timedelta
import urllib.parse
import html  #解碼用
import re

#------設定瀏覽器驅動程式與爬蟲網址------

chrome_options=ChromeOptions()
chrome_options.add_experimental_option("detach",True)
browser=webdriver.Chrome(options=chrome_options)
#browser.maximize_window()
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"""})
browser.get("https://icard.ai/home/all_cards")
time.sleep(5)
#browser.refresh() #重新整理
#time.sleep(2)
    
#------初始化------
x=0
df=pd.DataFrame(columns=["卡名","卡別","特色","說明"])


#------關閉cookie視窗------
elem=browser.find_element(By.XPATH,"//button[text()='關閉']") #找關閉按鈕
browser.execute_script("arguments[0].click();", elem);
time.sleep(1)

#------捲動畫面------
js="return document.body.scrollHeight"
new_height = browser.execute_script(js)
p=0
i=0
while True:
    p=p+1
    if p>10:  #捲動次數
        break
    i=i+500 #每次捲動高度
    browser.execute_script("window.scrollTo(0, %s)" % i) #每次捲動一定高度
    time.sleep(0.1)
    #print(i,new_height) #顯示指定高度值與視窗高度值
    new_height = browser.execute_script(js)  #紀錄目前視窗高度值
    if i>new_height:  #假如已捲超過視窗高度
        print("已經到頁面最底部，程序停止")
        break

#------點選展開全部下拉式按鈕------
elems=browser.find_elements(By.XPATH,"//div[@class='sc-yes8qh-0 accordion__item sc-9y76ir-1 iLqrqn']") #找優惠區塊
action = ActionChains(browser) #啟用滑鼠鍵盤操作
t=0
for elem in elems:
    action.move_to_element(elem)  #將游標移動到區塊物件上
    action.click() #在區塊物件上按下滑鼠左鍵
    action.perform() #執行滑鼠操作
    time.sleep(2)
    t=t+1
    if t>10 :  #展開優惠數量
        break


#------爬數據------
html_source=browser.page_source  #取得網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
cardarea=soup.find_all("div",class_="sc-o54cxr-0 bKzXFh") #找出信用卡區塊
for cards in cardarea:
    cardname=cards.find("div",class_="sc-fkouio-0 kMjtwV") #卡名
    cardclass=cards.find("div",class_="sc-fkouio-0 jsbhSP") #卡別
    print(cardname.text,cardclass.text)
    discountarea=cards.find_all("div",class_="sc-yes8qh-0 accordion__item sc-9y76ir-1 iLqrqn")  #找出優惠區塊
    for i in discountarea:
        discounttitle=i.find("div",class_="sc-fkouio-0 sc-9y76ir-2 ewghcY jcdfEI") #特色
        discountinfo=i.find("div",class_="sc-fkouio-0 sc-1fcwql5-0 WLCTt accordion__panel") #說明
        print(discounttitle.text)
        print("*******************")
        df.loc[x]=[cardname.text,cardclass.text,discounttitle.text,discountinfo.text]
        x=x+1

#------檔案儲存------
#df.to_csv("cards.csv",encoding="utf_8_sig")  #存成csv

#存成excel
writer=pd.ExcelWriter("cards.xlsx", engine = 'xlsxwriter')
df.to_excel(writer,sheet_name="信用卡數據")
writer.close()

browser.close()  #關閉瀏覽器