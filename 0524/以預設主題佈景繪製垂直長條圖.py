import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

election={'votes': [3690466, 5586019, 4671021],
          'candidates': ['KP', 'William', 'Friendship']}
data=pd.DataFrame(election)
sns.set()      # 使用預設主題佈景, 也可用 sns.set_theme()
sns.barplot(x='candidates', y='votes', data=data)
plt.title('2024 Presidential Election')
plt.xlabel('Candidates')
plt.ylabel('Votes(Million)')
plt.show()
