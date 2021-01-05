import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('temp_ice.csv', encoding='euc-kr')

data = np.array(df)
X = data[:, 1]
X = X.reshape(-1, 1)

Y = data[:, -1]
Y = Y.reshape(-1, 1)

reg = LinearRegression().fit(X, Y)

my_temp = float(input("안녕하세요. 오늘의 기온을 입력해 주세요. : "))

predicted_value = reg.predict(np.asarray(my_temp).reshape(-1, 1))

print("오늘의 아이스크림 쇼핑 클릭량은 100점을 기준으로 {0} 만큼 예상됩니다.".format(predicted_value))

'''
안녕하세요. 오늘의 기온을 입력해 주세요. : 30
오늘의 아이스크림 쇼핑 클릭량은 100점을 기준으로 [[63.93166397]] 만큼 예상됩니다.
'''
