import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import warnings

warnings.filterwarnings(action='ignore')

iris = pd.read_csv('Iris.csv')
 
xy = np.array(iris)
features = xy[:, 1:-1]
target_value = xy[:, [-1]]

neigh = KNeighborsClassifier(n_neighbors=3)

model = neigh.fit(features, target_value)

ID_1 = np.array([[2.7, 2.4, 1.65, 0.67]])
ID_2 = np.array([[5.84, 5.48, 3, 2.16]])
ID_3 = np.array([[3.97, 4.01, 1.7, 0.67]])

result_1 = model.predict(ID_1)
result_2 = model.predict(ID_2)
result_3 = model.predict(ID_3)

print(result_1,result_2,result_3)

'''
['Iris-setosa'] ['Iris-setosa'] ['Iris-setosa']
'''