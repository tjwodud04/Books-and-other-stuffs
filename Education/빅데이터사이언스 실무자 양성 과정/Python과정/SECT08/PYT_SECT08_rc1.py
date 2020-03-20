#01
result1 = list(range(10))
result2 = list(range(5, 10))
result3 = list(range(1, 10, 2))
print('range(10)     \t= ', result1)
print('range(5,10)   \t= ', result2)
print('range(1,10,2) \t= ', result3)
'''result
range(10)     	=  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(5,10)   	=  [5, 6, 7, 8, 9]
range(1,10,2) 	=  [1, 3, 5, 7, 9]
'''

#02
def add_txt(arg1, arg2):
    print(arg1, arg2)

param1 = '대~한민국~'
param2 = '짝짝~짝~ 짝.짝!!'
add_txt(param1, param2)
'''result
대~한민국~ 짝짝~짝~ 짝.짝!!
'''

#03
def add_num(num1, num2):
    result = num1 + num2
    return result

param1 = 40
param2 = 50
sum = add_num(param1, param2)
print('%d와 %d의 합은 %d입니다.' % (param1, param2, sum))
'''result
40와 50의 합은 90입니다.
'''

#04
def sayHello():
    print('Hi, Guys !!')

sayHello()
'''result
Hi, Guys !!
'''

#05
def exchangeUSDtoKRW(dollar):
    won = dollar * 1065
    return won

usd = 2000
krw = exchangeUSDtoKRW(usd)
print('환전한 금액은 %d 원 입니다.'%(krw))
'''result
환전한 금액은 2130000 원 입니다.
'''

#06
def calc_royalty(price, sales, per):
    rate = per / 100
    royalty = int(price * sales * rate)
    return royalty

i = input("책의 정가는？")
price = int(i)
i = input("발행 부수는？")
sales = int(i)
i = input("인세율(퍼센트)은？")
per = float(i)

v = calc_royalty(price, sales, per)
print("인세는 ", v, "원입니다.")
'''sample result
책의 정가는？27000
발행 부수는？1000
인세율(퍼센트)은？30
인세는  8100000 원입니다.
'''

#07
def orderMenu(menu):
    print('손님, %s를 주문하였습니다' % (menu))

orderMenu('카페모카')
'''result
손님, 카페모카를 주문하였습니다
'''

def orderCoffee(menu='카페라떼'):
    print('손님, %s를 주문하였습니다.' % (menu))

orderCoffee()
'''result
손님, 카페라떼를 주문하였습니다.
'''