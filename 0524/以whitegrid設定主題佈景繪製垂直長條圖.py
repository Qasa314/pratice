import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

election={'votes': [3690466, 5586019, 4671021],
          'candidates': ['KP', 'William', 'Friendship']}
data=pd.DataFrame(election)
pal=sns.color_palette() #設定調色盤
sns.set_theme(style='whitegrid')      # 使用預設主題佈景, 也可用 sns.set_theme()
sns.barplot(x='candidates', y='votes', data=data,palette=pal)
plt.title('2024 Presidential Election')
plt.xlabel('Candidates')
plt.ylabel('Votes(Million)')
plt.show()
