import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np    

votes=np.array([3690466, 5586019, 4671021])       # 轉成 ndarray 物件
candidates=['KP', 'William', 'Friendship']
sns.barplot(x=candidates, y=votes)
plt.title('2024 Presidential Election')
plt.xlabel('Candidates')
plt.ylabel('Votes(Million)')
plt.show()
