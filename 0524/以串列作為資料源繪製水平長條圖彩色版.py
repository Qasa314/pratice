import seaborn as sns
import matplotlib.pyplot as plt

votes=[3690466, 5586019, 4671021]      
candidates=['KP', 'William', 'Friendship']
pal=sns.color_palette() #設定調色盤
sns.barplot(x=votes, y=candidates,palette=pal)         # x 與 y 對調
plt.title('2024 Presidential Election')
plt.xlabel('Candidates')
plt.ylabel('Votes(Million)')
plt.show()

