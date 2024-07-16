import seaborn as sns
import matplotlib.pyplot as plt

votes=[3690466, 5586019, 4671021]      
candidates=['KP', 'William', 'Friendship']
sns.barplot(x=candidates, y=votes)     
plt.title('2024 Presidential Election')
plt.xlabel('Candidates')
plt.ylabel('Votes(Million)')
plt.show()

