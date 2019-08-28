#10
data   = (15, 50)
width, height = data
area = width * height

print('너비 :', width);
print('높이 :', height);
print('넓이 :', area)
'''result
너비 : 15
높이 : 50
넓이 : 750
'''

#11
lang = {'Java', 'Java', 'Python', 'C++', 'Python'}
print(lang)
print(type(lang))
print('Python'in lang)
print('Javascript'in lang)
'''result
{'Java', 'C++', 'Python'}
<class 'set'>
True
False
'''

#12
a = set('abracadabra')
b = set('alacazam')

print('집합 a =', a);  print('집합 b =', b);
print('합집합, a | b =', a | b)
print('교집합, a & b =', a & b)
print('차집합, a - b =', a - b)
print('여집합, a ^ b =', a ^ b)
'''result
집합 a = {'a', 'r', 'd', 'c', 'b'}
집합 b = {'a', 'c', 'l', 'z', 'm'}
합집합, a | b = {'a', 'r', 'd', 'c', 'b', 'l', 'z', 'm'}
교집합, a & b = {'a', 'c'}
차집합, a - b = {'b', 'r', 'd'}
여집합, a ^ b = {'b', 'r', 'l', 'd', 'z', 'm'}
'''

#13
beast = ["lion", "tiger", "wolf", "tiger", "lion", "bear", "lion" ]
print('beast =', beast)

unique_beast = list(set(beast))
print('unique_beast =', unique_beast)
sorted_beast = sorted(unique_beast)
print("sorted_beast =", sorted_beast)
'''result
beast = ['lion', 'tiger', 'wolf', 'tiger', 'lion', 'bear', 'lion']
unique_beast = ['lion', 'wolf', 'bear', 'tiger']
sorted_beast = ['bear', 'lion', 'tiger', 'wolf']
'''

#14
bans = { '잎새반':'찬영이',
         '열매반':'예영이',
         '햇살반':'준영이',
         '열매반':'채영이', }

print(type(bans))
print('반의수 : ', len(bans))

print('잎새반 : ', bans['잎새반'])
print('열매반 : ', bans['열매반'])
print('bans 읽기 :', bans)

bans['꽃잎반'] = '희영이'
print('bans 추가 :', bans)

bans['잎새반'] = '서영이'
print('bans 변경 :', bans)

del bans['햇살반']
print('bans 삭제 :', bans)
'''result
<class 'dict'>
반의수 :  3
잎새반 :  찬영이
열매반 :  채영이
bans 읽기 : {'잎새반': '찬영이', '열매반': '채영이', '햇살반': '준영이'}
bans 추가 : {'잎새반': '찬영이', '열매반': '채영이', '햇살반': '준영이', '꽃잎반': '희영이'}
bans 변경 : {'잎새반': '서영이', '열매반': '채영이', '햇살반': '준영이', '꽃잎반': '희영이'}
bans 삭제 : {'잎새반': '서영이', '열매반': '채영이', '꽃잎반': '희영이'}
'''

#15
customer = {
    "name"    : "김진수",
    'gender'  : '남자',
    "email"   : "bigpycraft@gmail.com",
    "company" : "빅파이크래프트",
    "address" : "서울시 중구 청파로"
}

print('customer.keys()   \t= ', customer.keys())
print('customer.values() \t= ', customer.values())
print('customer.items()  \t= ', customer.items())
print('-'*50)

for key, value in customer.items():
    print('%s\t : %s' %(key, value))
'''result
customer.keys()   	=  dict_keys(['name', 'gender', 'email', 'company', 'address'])
customer.values() 	=  dict_values(['김진수', '남자', 'bigpycraft@gmail.com', '빅파이크래프트', '서울시 중구 청파로'])
customer.items()  	=  dict_items([('name', '김진수'), ('gender', '남자'), ('email', 'bigpycraft@gmail.com'), ('company', '빅파이크래프트'), ('address', '서울시 중구 청파로')])
--------------------------------------------------
name	 : 김진수
gender	 : 남자
email	 : bigpycraft@gmail.com
company	 : 빅파이크래프트
address	 : 서울시 중구 청파로
'''