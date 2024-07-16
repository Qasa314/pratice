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

'''
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
'''
chrome_options.add_experimental_option("detach",True)
browser=webdriver.Chrome(options=chrome_options)
browser.get("https://icard.ai/home/all_cards")
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

#展開所有卡片
elems=browser.find_elements(By.XPATH,"//div[@class='sc-fkouio-0 sc-1twl20m-0 dsznjQ bjXwWV']") #找展開卡片的元件
action=ActionChains(browser) #啟用滑鼠鍵盤操作
for elem in elems:
    action.move_to_element(elem) #將游標移動到展開按鈕元件上
    action.click() #在元件上按下滑鼠左鍵
    action.perform() #執行滑鼠操作
    time.sleep(2)
    print("展開")
    

time.sleep(5)
#宣告變數值
df=pd.DataFrame(columns=["卡名","卡別"])  #宣告空的df



#爬大區塊
html_source=browser.page_source  #取得網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
area1=soup.find_all("div",class_="sc-o54cxr-0 bKzXFh")   #信用卡區塊
print(area1[0].text)

'''
#爬細節
x=0
for i in range(0,len(area1),1):
    area2=area1[i].find_all("div",class_="sc-fkouio-0 jdQMAt")
    print("數量",len(area2))
    for j in area2:
        cardname=j.find("div",class_="sc-fkouio-0 kMjtwV").text
        cardclass=j.find("div",class_="sc-fkouio-0 jsbhSP").text
        
        print("卡名:",cardname)
        print("卡別:",cardclass)
        print("------------------")    
        df.loc[x]=[cardname,cardclass]  #紀錄存到pandas
        x=x+1


#儲存成檔案
#df.to_csv("cards.csv",encoding="utf_8_sig")  #存成csv
#存成excel
writer=pd.ExcelWriter("cards.xlsx", engine = 'xlsxwriter')
df.to_excel(writer,sheet_name="cards")
writer.close()
'''
browser.close()