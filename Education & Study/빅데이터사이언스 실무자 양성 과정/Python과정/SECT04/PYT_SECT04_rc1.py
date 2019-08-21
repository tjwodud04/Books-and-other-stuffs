#01
x = 50
y = 4.

print("x = ", x)
print("y = ", y)
print("x + y = " , x+y)
print("x - y = " , x-y)
print("x * y = " , x*y)
print("x / y = " , x/y)
'''result
x =  50
y =  4.0
x + y =  54.0
x - y =  46.0
x * y =  200.0
x / y =  12.5
'''

#02
print("x //y = " , x//y)
print("x % y = " , x%y)
print("-x = "    , -x)
print("+x = "    , +x)
print("x ** y = ", x**y)
print("pow(x,y) = ", pow(x,y))
'''result
x //y =  12.0
x % y =  2.0
-x =  -50
+x =  50
x ** y =  6250000.0
pow(x,y) =  6250000.0
'''

#03
x = 4
y = 9

print("x == y = ", x==y)
print("x != y = ", x!=y)

print("x < y  = ", x<y)
print("x > y  = ", x>y)

print("int(True)  = ", int(True))
print("int(False) = ", int(False))
'''result
x == y =  False
x != y =  True
x < y  =  True
x > y  =  False
int(True)  =  1
int(False) =  0
'''

#04
text1 = "안녕하세요! \n데이터사이언스과정\t수강생여러분 !"

text2 = '''\
빅데이터를 위한 파이썬과정에서
만나뵙게되어 반갑습니다.
끝까지 '화이팅' 하세요!!!\
'''
print(text1)
print("-"*50)
print(text2)
#------------
'''result
안녕하세요! 
데이터사이언스과정	수강생여러분 !
--------------------------------------------------
빅데이터를 위한 파이썬과정에서
만나뵙게되어 반갑습니다.
끝까지 '화이팅' 하세요!!!
'''

#05
test = '파이썬 프로그래밍 재미있다!'
result = test.startswith('파이썬')
print(result)
result = test.endswith('!')
print(result)
result = test.endswith('어려워요!')
print(result)
result = test.replace('파이썬', 'Python')
print(result)

'''result
True
True
False
Python 프로그래밍 재미있다!
'''