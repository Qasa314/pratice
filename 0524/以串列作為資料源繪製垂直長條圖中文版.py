import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager #字型管理

votes=[3690466, 5586019, 4671021]   
candidates=['老柯', '賴神', '友誼']

#列出內建可用字型
font_set = {f.name for f in font_manager.fontManager.ttflist}
for f in font_set:
    print(f)

#掛上微軟正黑體
rc = {'font.family': 'Microsoft JhengHei',
      'axes.unicode_minus': False}
sns.set(rc=rc)
sns.barplot(x=candidates, y=votes)     
plt.title('2024總統大選')
plt.xlabel('候選人')
plt.ylabel('得票數(百萬)')
plt.show()
