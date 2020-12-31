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

#평균 기온 값을 기준으로 도수분포 구간 설정하기
bins = np.arange(min(temp),max(temp),5)

print(bins)

'''
[-3.8  1.2  6.2 11.2 16.2 21.2 26.2]
'''