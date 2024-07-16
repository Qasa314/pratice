'''
文字雲需要安裝套件
pip install wordcloud 
pip install jieba
'''
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import jieba
import jieba.analyse
from collections import Counter # 次數統計

dictfile = "dict.txt.big.txt"  #設定常用字典
stopfile = "stopWord.txt"  #設定停用詞，譬如唱歌會用到的oh，喔
fontpath = "msjh.ttf"  #中文繪圖需要中文字體,微軟正黑體
userdict="userdict.txt" #設定自訂的字典,就是一定要保留的，譬如五月天的 "動次"
mdfile = "lyrics.txt"  #要分析的來源，這個範例是五月天20首歌
topwords=1 #使用排名前幾個的字詞
pngfile = "mask_Tiara.png"  #想要文字雲出現的遮罩圖案(單色,png檔案背景不可透明)
outputfile="Mayday_Wordcloud.png"  #輸出圖片檔案名稱

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
