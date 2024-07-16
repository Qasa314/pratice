import seaborn as sns
#列出官方提供的範例數據資料名稱
print(sns.get_dataset_names())
#載入鳶尾花數據
df=sns.load_dataset('iris')
print(df.head())
