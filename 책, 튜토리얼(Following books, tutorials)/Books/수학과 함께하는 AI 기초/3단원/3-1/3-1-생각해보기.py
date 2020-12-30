# K-평균 군집화 알고리즘 적용하기 - 생각해보기
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

fifa2019 = pd.read_csv('fifa2019.csv')
df = pd.DataFrame.copy(fifa2019.sort_values(by = 'Overall', ascending = False ).head(200))
test_features = ['Name','Stamina','Dribbling','ShortPassing','Penalties']
test_df = pd.DataFrame(df , columns = test_features)

XY = np.array(test_df)
X = XY[:,1:3]

kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

prediction = kmeans.predict(X)

print(prediction)

'''
[0 0 0 1 0 0 0 0 2 2 0 1 0 0 0 2 0 1 0 0 1 1 0 0 0 2 1 1 2 0 1 0 0 0 0 0 0
 0 0 0 0 0 0 2 0 0 2 0 0 0 1 0 2 0 2 0 0 0 0 2 0 2 2 0 0 0 1 0 0 2 0 0 2 0
 0 0 0 0 0 0 0 0 2 0 2 0 2 0 0 2 0 2 2 0 0 0 2 0 0 1 1 0 0 0 0 0 2 2 0 0 0
 0 1 0 0 0 0 0 0 0 0 0 2 1 2 1 2 0 2 0 0 1 0 1 0 0 2 0 0 2 0 0 0 2 2 0 2 0
 0 2 1 1 0 0 0 0 0 0 2 0 1 0 0 0 1 1 0 0 0 0 0 1 2 0 1 2 1 0 0 2 0 1 0 2 1
 1 1 0 2 2 1 0 0 0 0 0 2 0 0 0]
'''

plt.scatter(X[prediction == 0,0], X[prediction == 0,1], s=50, c='red', marker='o', edgecolor='black', label='A')
plt.scatter(X[prediction == 1,0], X[prediction == 1,1], s=50, c='yellow', marker='x', edgecolor='black', label='B')
plt.scatter(X[prediction == 2,0], X[prediction == 2,1], s=50, c='blue', marker='^', edgecolor='black', label='C')

plt.legend()
plt.grid()
plt.show()
