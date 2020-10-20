# 일주일 간 유동인구 데이터 (월요일 ~ 일요일)
a = [242, 256, 237, 223, 263, 81, 46]

# -----------------------------------------------------------
# 유동 인구 데이터의 총합과 평균 구하기

n = len(a)
my_sum = 0
my_avg = 0
i = 0

for i in range (0, n) :
    my_sum = my_sum + a[i]

my_avg = my_sum/n

print("Total Sum : ", my_sum)
print("Total Average : ", my_avg)
'''
Total Sum :  1348
Total Average :  192.57142857142858
'''