import csv
import matplotlib.pyplot as plt
import numpy as np

f = open('temp_ice.csv', encoding='euc-kr')
data = csv.reader(f)
header = next(data)
temp = []
ice = []

# 전체 데이터를 행별로 temp 리스트, ice 리스트에 저장 및 출력하기
for row in data :
    temp.append(float(row[1]))
    ice.append(int(row[4]))

# 평균 기온 값을 기준으로 도수 분포 구간 설정
bins = np.arange(min(temp),max(temp)+5,5)

# 각 계급에 해당하는 도수값 확인 후 출력하기
hist, bins = np.histogram(temp, bins)

# 평균 기온값을 기준으로 아이스크림 쇼핑 클릭량을 구분하여 저장하기
ice_buy = np.zeros(7)

for i in range(0,len(temp)) :
    for j in range(0, len(bins)):
        if j == len(bins):
            ice_buy[j] = ice_buy[j] + ice[i]
        else:
            if bins[j] <= temp[i] and temp[i] < bins[j+1]:
                ice_buy[j] = ice_buy[j] + ice[i]

# 계급별 아이스크림 쇼핑 클릭량의 평균을 구하기
# 평균 기온값 계급별 아이스크림 쇼핑 클릭량의 평균 구하기
ice_buy_a = np.zeros(7)

for i in range(0,len(ice_buy)) :
    ice_buy_a[i] = ice_buy[i] / hist[i]

# 평균 기온에 따른 아이스크림 쇼핑 클릭량의 평균을 막대그래프로 표현하기
plt.xlabel('Average temperature')
plt.ylabel('Number of ice cream shopping')

# 평균 기온값 계급별 아이스크림 쇼핑 클릭량의 평균값을 분산형 그래프로 나타내기
plt.scatter(temp, ice)
plt.show()
