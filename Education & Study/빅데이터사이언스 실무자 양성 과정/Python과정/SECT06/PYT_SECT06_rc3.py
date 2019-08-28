#13
sigmal_color = ''

while sigmal_color != 'blue' and sigmal_color != 'red':
    sigmal_color = input('색을 영문으로 입력하세요 (blue/red) : ')

    if sigmal_color == 'blue':
        print('신호등은 파란색 입니다. 길을 건너세요!!')
    elif sigmal_color == 'red':
        print('신호등은 빨간색 입니다. 기다리세요.')
    else:
        print('잘못된 색입니다. 다시 입력해 주세요!!')

print('프로그램을 종료합니다.')
'''sample result
색을 영문으로 입력하세요 (blue/red) : yellow
잘못된 색입니다. 다시 입력해 주세요!!
색을 영문으로 입력하세요 (blue/red) : blue
신호등은 파란색 입니다. 길을 건너세요!!
프로그램을 종료합니다.
'''

#14
result = list(range(10))
print('range(10)     :', result)

result = list(range(5,10))
print('range(5,10)   :', result)

result = list(range(1,10,2))
print('range(1,10,2) :', result)
'''result
range(10)     : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(5,10)   : [5, 6, 7, 8, 9]
range(1,10,2) : [1, 3, 5, 7, 9]
'''

#15
scope = [1, 2, 3, 4, 5]

for x in scope:
    print(x)
'''result
1
2
3
4
5
'''

#16
scope = list(range(1, 100))

for num in scope:

    if num <= 10:
        if num % 2 == 0:
            pass
            print(num, 'is even number.')
        else:
            continue
            print(num, 'is odd number.')
    else:
        print(num, 'is bigger than ten')
        break
        print('after break')

print('프로그램을 종료합니다.')
'''result
2 is even number.
4 is even number.
6 is even number.
8 is even number.
10 is even number.
11 is bigger than ten
프로그램을 종료합니다.
'''

#17
for i in range(1, 10, 2):
    mark = "*" * i
    print(mark)
'''result
*
***
*****
*******
*********
'''
for i in range(1, 10, 2):
    mark = " " * int((10-i)/2) + "*" * i
    print(mark)
'''result
    *
   ***
  *****
 *******
*********
'''

#18
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for x in range(3):
    for y in range(3):
        print('matrix[%d][%d]:'%(x, y), matrix[x][y], end=' \t')
    else:
        print('')
'''result
matrix[0][0]: 1 	matrix[0][1]: 2 	matrix[0][2]: 3 	
matrix[1][0]: 4 	matrix[1][1]: 5 	matrix[1][2]: 6 	
matrix[2][0]: 7 	matrix[2][1]: 8 	matrix[2][2]: 9
'''