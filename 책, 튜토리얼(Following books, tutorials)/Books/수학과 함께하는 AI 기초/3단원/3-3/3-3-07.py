import csv
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
    if bins[0] <= temp[i] and temp[i] < bins[1] :
        ice_buy[0] = ice_buy[0] + ice[i]
        
    elif bins[1] <= temp[i] and temp[i] < bins[2] :
        ice_buy[1] = ice_buy[1] + ice[i]
        
    elif bins[2] <= temp[i] and temp[i] < bins[3] :
        ice_buy[2] = ice_buy[2] + ice[i]

    elif bins[3] <= temp[i] and temp[i] < bins[4] :
        ice_buy[3] = ice_buy[3] + ice[i]
        
    elif bins[4] <= temp[i] and temp[i] < bins[5] :
        ice_buy[4] = ice_buy[4] + ice[i]
        
    elif bins[5] <= temp[i] and temp[i] < bins[6] :
        ice_buy[5] = ice_buy[5] + ice[i]
        
    else:
        ice_buy[6] = ice_buy[6] + ice[i]

# 계급별 아이스크림 쇼핑 클릭량의 평균을 구하기
# 평균 기온값 계급별 아이스크림 쇼핑 클릭량의 평균 구하기
ice_buy_a = np.zeros(7)

for i in range(0,len(ice_buy)) :
    ice_buy_a[i] = ice_buy[i] / hist[i]


for i in range(0,len(ice_buy)):
    print('%0.2f'%ice_buy_a[i])

'''
27.45
28.29
29.38
33.31
56.11
54.21
62.15
'''