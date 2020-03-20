#01
condition = False

if condition:
    print("조건을 충족함, condition met")

if not condition:
    print("조건 충족 못함, condition not met")
'''result
조건 충족 못함, condition not met
'''

#02
num_a = 100
num_b = 200

if num_a > num_b:
    print('숫자A가 숫자B보다 더 큰수입니다.')
else:
    print('숫자A는 숫자B와 같거나 더 작은수입니다.')
'''result
숫자A는 숫자B와 같거나 더 작은수입니다.
'''

#03
num_a = 100
num_b = 200

if num_a > num_b:
    print('숫자A가 더 큰수입니다.')
    max = num_a
elif num_a < num_b:
    print('숫자B가 더큰수입니다.')
    max = num_b
else:
    print('숫자A와 숫자B는 같습니다.')

print('숫자A와 숫자B중 최대값은', max, '입니다.')
'''result
숫자B가 더큰수입니다.
숫자A와 숫자B중 최대값은 200 입니다.
'''

#04
signal_color = input('색을 영문으로 나타내어 보세요.')

if signal_color == 'blue':
    print('신호등은 파란색 입니다. 건너가 주세요.')
else:
    print('신호등은 빨간색 입니다. 기다려 주세요.')
'''result
색을 영문으로 나타내어 보세요.blue
신호등은 파란색 입니다. 건너가 주세요.
'''

#05
signal_color = input('색을 영문으로 나타내어 보세요. (blue/red) ')

if signal_color == 'blue':
    print('신호등은 파란색 입니다. 건너가 주세요.')
elif signal_color == 'red':
    print('신호등은 빨간색 입니다, 기다려 주세요.')
else:
    print('잘못된 색입니다')
'''result
색을 영문으로 나타내어 보세요. (blue/red) red
신호등은 빨간색 입니다, 기다려 주세요.
'''

#06
signal_color = input('색을 영문으로 나타내어 보세요.')

if signal_color == 'blue':
    print('신호등은 파란색 입니다. 건너가 주세요.')
    is_pass = input('건널 준비가 되셨나요? (yes/no) ')

    if is_pass == 'yes':
        print('네, 건너겠습니다.')
    else:
        print('다음 번에 건너겠습니다.')
elif signal_color == 'red':
    print('신호등은 빨간색 입니다, 기다려 주세요.')
else:
    print('잘못된 색입니다')
'''result
색을 영문으로 나타내어 보세요.blue
신호등은 파란색 입니다. 건너가 주세요.
건널 준비가 되셨나요? (yes/no) yes
네, 건너겠습니다.
'''

#07
weight = float(input("체중(kg)은 ? "))
height = float(input("키(cm)는 ? "))

height = height / 100
bmi = weight / (height * height)

result = ""
if bmi < 18.5:
    result = "마름"
if (18.5 <= bmi) and (bmi < 25):
    result = "보통"
if (25 <= bmi) and (bmi < 30):
    result = "가벼운 비만"
if bmi >= 30:
    result = "심한 비만"

print('-'*50)
print("BMI :", bmi)
print("판정:", result)
'''sample result
체중(kg)은 ? 68
키(cm)는 ? 172
--------------------------------------------------
BMI : 22.985397512168742
판정: 보통
'''