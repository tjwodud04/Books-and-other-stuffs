import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('pima-indians-diabetes.csv', names=["pregnant","plasma","pressure","thickness","insulin","BMI","pedigree","age","class"])

print(df.head(5), "\n")
print(df.info(), "\n")
print(df.describe(), "\n")
print(df[['pregnant','class']].groupby(['pregnant'],as_index=False).mean().sort_values(by='pregnant', ascending=True), "\n")

plt.figure(figsize=(9,9))
sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=plt.cm.gist_heat, linecolor='white', annot=True)
plt.show()

grid = sns.FacetGrid(df, col='class')
grid.map(plt.hist, 'plasma', bins=10)
plt.show()