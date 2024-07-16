import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

election={'votes': [3690466, 5586019, 4671021],
          'candidates': ['KP', 'William', 'Friendship']}
data=pd.DataFrame(election)
sns.set_style('dark', {'axes.edgecolor': 'white', 'axes.facecolor': 'white'}) #全部改白色就成了無框圖
sns.barplot(x='candidates', y='votes', data=data)
#sns.despine()   #去除右邊框與上邊框 
plt.title('2024 Presidential Election')
plt.xlabel('Candidates')
plt.ylabel('Votes(Million)')
plt.show()

