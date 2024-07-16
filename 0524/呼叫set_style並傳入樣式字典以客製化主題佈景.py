import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

election={'votes': [3690466, 5586019, 4671021],
          'candidates': ['KP', 'William', 'Friendship']}
data=pd.DataFrame(election)
print(sns.axes_style()) #列出目前樣式設定
print("---------------")
sns.set_style('dark', {'axes.edgecolor': 'blue', 'axes.facecolor': 'cyan'})
print(sns.axes_style()) #列出目前樣式設定
sns.barplot(x='candidates', y='votes', data=data)
plt.title('2024 Presidential Election')
plt.xlabel('Candidates')
plt.ylabel('Votes(Million)')
plt.show()
