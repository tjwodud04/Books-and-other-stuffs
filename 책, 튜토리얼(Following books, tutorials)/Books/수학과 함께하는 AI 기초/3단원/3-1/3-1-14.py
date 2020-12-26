# 각 표본에 가까운 중심에 할당하기
import pandas as pd
import numpy as np

fifa2019 = pd.read_csv('fifa2019.csv')
df = pd.DataFrame.copy(fifa2019.sort_values(by = 'Overall', ascending = False ).head(200))
test_features = ['Name','Stamina','Dribbling','ShortPassing','Penalties']
test_df = pd.DataFrame(df , columns = test_features)

XY = np.array(test_df)
X = XY[:,1:3]

k = 3
C_x = np.random.choice(X[:,0],k)
C_y = np.random.choice(X[:,1],k)
C = np.array(list(zip(C_x, C_y)))

def Distance(A, B):
    return np.sqrt(np.sum(np.power((A-B),2)))

C_old = np.zeros(C.shape)
clusters = np.zeros(len(X))
flag = Distance(C, C_old)

print(C_old)
print(flag)

'''
[[0. 0.]
 [0. 0.]
 [0. 0.]]
163.72843369433423
'''