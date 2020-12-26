# 표본공간에 k개의 중심을 무작위로 생성하여 그 생성 결과를 시각적으로 확인하기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fifa2019 = pd.read_csv('fifa2019.csv')
df = pd.DataFrame.copy(fifa2019.sort_values(by = 'Overall', ascending = False).head(200))
test_features = ['Name','Stamina','Dribbling','ShortPassing','Penalties']

test_df = pd.DataFrame(df, columns = test_features)

XY = np.array(test_df)
X = XY[:,1:3]

k = 3
C_x = np.random.choice(X[:,0],k)
C_y = np.random.choice(X[:,1],k)
C = np.array(list(zip(C_x, C_y)))

Stamina = test_df['Stamina']
Dribbling = test_df['Dribbling']

plt.title('Stamina&Dribbling')
plt.xlabel('Stamina')
plt.ylabel('Dribbling')

plt.scatter(Stamina,Dribbling,marker='^',c='blue',s=10,label='players')
plt.scatter(C_x, C_y, marker='*', s=200, c='black',label='centroids')

plt.legend(loc='best')

plt.grid()
plt.show()
