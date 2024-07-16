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

chrome_options=ChromeOptions()
chrome_options.add_experimental_option("detach",True)
browser=webdriver.Chrome(options=chrome_options)
browser.get("https://mops.twse.com.tw/mops/web/t78sb04_q2")


time.sleep(2)

elem=browser.find_element("id","year")
elem.send_keys("113")

select=Select(browser.find_element("id","season"))
select.select_by_index(1)

search=browser.find_element(By.XPATH,"/html/body/center/table/tbody/tr/td/div[4]/table/tbody/tr/td/div/table/tbody/tr/td[3]/div/div[3]/form/table/tbody/tr/td[4]/table/tbody/tr/td[2]/div/div/input")
search.click()

time.sleep(5)













list1=[]
html_source=browser.page_source  #取得網頁原始碼
soup=BeautifulSoup(html_source,"lxml")
area1=soup.find_all("table",class_="hasBorder")
area2=area1[0].find_all("tr")
for i in range(1,51,1):
    area3=area2[i].find_all("td")
    list1.append(area3[0].text)
    
print(list1)
    
    







browser.close()