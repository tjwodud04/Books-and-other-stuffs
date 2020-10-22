# 정리한 데이터를 꺾은선 그래프로 표현하기

import csv

a = [[],[],[],[],[],[],[]]

with open('passby_data.csv', 'r') as f :
    reader = csv.DictReader(f)
    i = j = 0

    for row in reader :        
        a[i].append(row)
        j = j + 1

        if j % 24 == 0 :
            i = i + 1

day_title = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
hour_title = ['01', '02', '03', '04', '05', '06', \
                '07', '08','09', '10', '11', '12', \
                '13', '14','15', '16', '17', '18', \
                '19', '20','21', '22', '23', '24',]

avgh= []

for j in range(0, 24) :                              
    day_sum = 0

    for i in range (0, 7) :
        day_sum = day_sum + int(a[i][j]['num'])

    avgh.append(day_sum/7)

# ----------------------------------------------------------------------
import matplotlib.pyplot as plt

plt.title("hourly passerby data", fontsize = 16)
plt.xlabel("hour", fontsize=10)
plt.ylabel("number of passerby", fontsize=12)

plt.scatter(hour_title, avgh)
plt.plot(hour_title, avgh)
plt.show()
