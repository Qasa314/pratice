def getmoney():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options as ChromeOptions  #2023改版
    from bs4 import BeautifulSoup
    import time

    money=[]
    chrome_options=ChromeOptions()
    chrome_options.add_experimental_option("detach",True)
    browser=webdriver.Chrome(options=chrome_options)
    browser.get("https://www.taiwanlottery.com/lotto/lotto_lastest_result")
    time.sleep(5)
    html_source=browser.page_source  #取得網頁原始碼
    soup=BeautifulSoup(html_source,"lxml")
    area1=soup.find_all("div",class_="custom-table-root lottery-distribution-table-root")
    area2=area1[1].find_all("div",class_="td-box")
    for i in range(5,50,6):
        money.append(area2[i].text)
    browser.close()
    return money
    