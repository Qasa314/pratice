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
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import jieba
import jieba.analyse
from collections import Counter # 次數統計


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

df=pd.DataFrame(columns=["標題"])  #宣告空的df

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
            df.loc[i]=[title1]
        else:
            break#小的就斷掉
df.to_csv("ds.csv",encoding="utf_8_sig")
browser.close()


dictfile = "dict.txt.big.txt"  #設定常用字典
stopfile = "stopWord.txt"  #設定停用詞，譬如唱歌會用到的oh，喔
fontpath = "msjh.ttf"  #中文繪圖需要中文字體,微軟正黑體
userdict="userdict.txt" #設定自訂的字典,就是一定要保留的，譬如五月天的 "動次"
mdfile = "ds.csv"  #要分析的來源，這個範例是五月天20首歌
topwords=100 #使用排名前幾個的字詞
pngfile = "mask_Tiara.png"  #想要文字雲出現的遮罩圖案(單色,png檔案背景不可透明)
outputfile="東森文字雲.png"  #輸出圖片檔案名稱

bgmask = np.array(Image.open(pngfile))

jieba.set_dictionary(dictfile)
jieba.analyse.set_stop_words(stopfile)
jieba.load_userdict(userdict)
text = open(mdfile,"r",encoding="utf-8").read()
tags = jieba.analyse.extract_tags(text, topK=topwords)
seg_list = jieba.lcut(text, cut_all=False)
dictionary = Counter(seg_list)

#開始段詞與排序
freq = {}
for ele in dictionary:
    if ele in tags:
        freq[ele] = dictionary[ele]
print(freq) # 計算各詞彙出現的次數

#背景顏色預設黑色，改為白色
#遮罩圖案改用五月天的皇冠
#contour是指邊框
#margin是文字間距
#其他參數請自行參考wordcloud
wordcloud = WordCloud(background_color="white", mask=bgmask, contour_width=3, contour_color='steelblue', font_path= fontpath).generate_from_frequencies(freq)
#wordcloud = WordCloud(background_color="white", mask=bgmask, font_path= fontpath, width=2400, height=2400, margin=0).generate_from_frequencies(freq)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
#存檔用
plt.savefig(outputfile)
#顯示用
plt.show()