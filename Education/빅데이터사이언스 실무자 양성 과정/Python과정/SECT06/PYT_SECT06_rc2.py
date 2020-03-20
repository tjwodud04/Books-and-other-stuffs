#08
children = int(input("어린이 요금(13세 미만)은 몇 명? "))
normal = int(input("보통 요금(13세~64세)은 몇 명? "))
elder = int(input("경로우대요금(65세 이상)은 몇 명? "))

total_num = children + normal + elder
children_price = children * 500
normal_price = normal * 1000
elder_price = elder * 700
total_price = children_price + normal_price + elder_price

if total_num >= 10:
    print("단체 할인됩니다.")
    total_price = total_price * 0.8
else:
    print("단체 할인되지 않습니다.")

print('-'*50)
print("어린이 요금 \t: {0}명x 500 = {1}원".format(children, children_price))
print("보통 요금   \t: {0}명x1000 = {1}원".format(normal, normal_price))
print("경로우대요금\t: {0}명x 700 = {1}원".format(elder, elder_price))
print('-'*50)
print("합계: {0}人 {1}원".format(total_num, total_price))
'''sample result
어린이 요금(13세 미만)은 몇 명? 3
보통 요금(13세~64세)은 몇 명? 5
경로우대요금(65세 이상)은 몇 명? 2
단체 할인됩니다.
--------------------------------------------------
어린이 요금 	: 3명x 500 = 1500원
보통 요금   	: 5명x1000 = 5000원
경로우대요금	: 2명x 700 = 1400원
--------------------------------------------------
합계: 10人 6320.0원
'''

#09
year = int(input("서기 몇 년 ? "))

is_leap = (year % 400 == 0)or((year % 100 != 0)and(year % 4 == 0))

if is_leap:
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")
'''sample result
서기 몇 년 ? 2020
윤년입니다.
'''

#10
idx = 0

while idx < 5:
    print(idx)
    idx += 1

print('프로그램 종료!')
'''result
0
1
2
3
4
프로그램 종료!
'''

#11
num, sum = 1, 0

while True:
    sum += num
    if sum > 100:
        break
    else:
        num += 1

print('num 값이 %d 일때 while문 탈출 !!' % num)
'''result
num 값이 14 일때 while문 탈출 !!
'''

#12
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
idx, sum = 0, 0

while idx < len(numbers):
    num = numbers[idx]
    sum += idx
    idx += 1

print('numbers의 합계는', sum, '입니다.')
'''result
numbers의 합계는 45 입니다.
'''