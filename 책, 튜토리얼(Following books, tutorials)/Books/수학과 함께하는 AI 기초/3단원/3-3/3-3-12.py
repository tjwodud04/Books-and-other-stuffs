# 데이터를 학습, 평가 데이터로 분리하기
# 데이터 준비하기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('temp_ice.csv', encoding='euc-kr')

# 학습(train) 데이터를 입력 변수와 출력 변수로 나누기
data = np.array(df)
X = data[:, 1]
Y = data[:, -1]

# 비용을 계산하고 업데이트하기
# 입력 변수와 출력 변수 각각의 평균(mean) 구하기
mean_x = np.mean(X)
mean_y = np.mean(Y)

# X변수의 개수 구하기
n = len(X)

# 최소제곱법을 이용하여 beta0과 beta1 구하기
temp1 = 0
temp2 = 0

for i in range(n):
  temp1 += (X[i] - mean_x) * (Y[i] - mean_y)
  temp2 += (X[i] - mean_x) ** 2

beta1 = temp1 / temp2
beta0 = mean_y - (beta1 * mean_x)
 
# 학습 결과 시각화하기
Y_pred = beta0+beta1*X

plt.title('Avg_temp & Clicks')
plt.xlabel('Average temperature(C)')
plt.ylabel('Clicks')
plt.plot(X,Y,'k.')
plt.plot(X,Y_pred, color='red')
plt.axis([-4,30,20,100])
plt.grid()
plt.show()
