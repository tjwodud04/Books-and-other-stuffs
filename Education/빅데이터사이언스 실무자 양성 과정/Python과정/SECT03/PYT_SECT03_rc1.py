#01
print('Hello, Python !!')
print('반갑습니다. \n파이썬세계로 온것을 환영합니다.')
print("문자는 반드시 인용부호(\' \' 혹은 \" \")로 감싸야 합니다.")
''' result
Hello, Python !!
반갑습니다. 
파이썬세계로 온것을 환영합니다.
문자는 반드시 인용부호(' ' 혹은 " ")로 감싸야 합니다.
'''

#02
print(100)
print(150 + 200)
print(150 - 200)
''' result
100
350
-50
'''

#03
print(100)
print(150 + 200)
print(150 - 200)
''' result
100
350
-50
'''

#04
x = 50
y = 4.

print("x = ", x)
print("y = ", y)
print("x + y = " , x+y)
print("x - y = " , x-y)
print("x * y = " , x*y)
print("x / y = " , x/y)
print("x //y = " , x//y)
print("x % y = " , x%y)
print("-x = "    , -x)
print("+x = "    , +x)
print("x ** y = ", x**y)
print("pow(x,y) = ", pow(x,y))
'''result
x =  50
y =  4.0
x + y =  54.0
x - y =  46.0
x * y =  200.0
x / y =  12.5
x //y =  12.0
x % y =  2.0
-x =  -50
+x =  50
x ** y =  6250000.0
pow(x,y) =  6250000.0
'''

#05
name = '홍길동'
greeting = '안녕'

print(name, greeting)
print(greeting, name)

text = name + '님, ' + greeting + '하세요'
print(text)
'''result
홍길동 안녕
안녕 홍길동
홍길동님, 안녕하세요
'''

#06
coffee1_name = '카페라떼';  coffee1_val = 4000;
coffee2_name = '카푸치노';  coffee2_val = 4500;
coffee3_name = '마끼야또';  coffee3_val = 5000;
'''Type Error Case
print('손님, ' + coffee1_name + coffee2_name + coffee3_name + '를 주문하셨습니다.')
print('가격은 ' + coffee1_val + coffee2_val + coffee3_val + '원 입니다.')
'''
print('손님, ' + coffee1_name + coffee2_name + coffee3_name + '를 주문하셨습니다.')
print('가격은 ' + str(coffee1_val + coffee2_val + coffee3_val) + '원 입니다.')
'''result
손님, 카페라떼카푸치노마끼야또를 주문하셨습니다.
가격은 13500원 입니다.
'''