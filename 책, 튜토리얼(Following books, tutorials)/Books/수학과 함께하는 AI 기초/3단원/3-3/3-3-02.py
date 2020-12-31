import csv

f = open('temp_ice.csv', encoding='euc-kr')
data = csv.reader(f)
header = next(data)
temp = []
ice = []

# 전체 데이터를 행별로 temp 리스트, ice 리스트에 저장 및 출력하기
for row in data :
    temp.append(float(row[1]))
    ice.append(int(row[4]))

print(min(temp), max(temp))

'''
-3.8 28.8
'''