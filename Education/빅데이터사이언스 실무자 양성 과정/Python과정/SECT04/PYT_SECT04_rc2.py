#06
test = 'Python Programming is Interesting!'
result = test.upper()
print(result)
result = test.lower()
print(result)
result = '/'.join(test)
print(result)
'''result
PYTHON PROGRAMMING IS INTERESTING!
python programming is interesting!
P/y/t/h/o/n/ /P/r/o/g/r/a/m/m/i/n/g/ /i/s/ /I/n/t/e/r/e/s/t/i/n/g/!
'''

#07
num_data = 350
str_data = '350'

print(type(num_data))
print(type(str_data))
'''result
<class 'int'>
<class 'str'>
'''

#08
sum = int(str_data) + num_data
print('합계는? ', str(sum))
'''result
합계는?  700
'''

#09
hello = '안녕하세요!'
print(hello)
print(id(hello))
hello = '반값습니다!'
print(hello)
print(id(hello))
'''result
안녕하세요!
1640034586672
반값습니다!
1640034588576
'''

#10
hello_list = ['안녕하세요!']
print(hello_list)
print(id(hello_list))
hello_list[0] = '반갑습니다!'
print(hello_list)
print(id(hello_list))
'''result
['안녕하세요!']
1640034008456
['반갑습니다!']
1640034008456
'''