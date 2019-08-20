#07
name = input('당신의 이름은 무엇입니까? ')
print(name + '님, 반갑습니다.')

#08
order = input('OO카페입니다. \n무엇을 주문하시겠습니까? ')
count = input('몇 잔을 드릴까요? ')
print('%s %s잔을 주문하셨습니다. \n잠시만 기다려주세요~^^' % (order, count))
'''sample result
OO카페입니다. 
무엇을 주문하시겠습니까? 아메리카노
몇 잔을 드릴까요? 3
아메리카노 3잔을 주문하셨습니다. 
잠시만 기다려주세요~^^
'''

#09
price = 4500
cost  = price * int(count)
print('%s %s잔을 주문하셨습니다. \n결재하실 금액은 %d원입니다~^^' % (order, count, cost))
'''sample result
아메리카노 2잔을 주문하셨습니다. 
결재하실 금액은 9000원입니다~^^
'''