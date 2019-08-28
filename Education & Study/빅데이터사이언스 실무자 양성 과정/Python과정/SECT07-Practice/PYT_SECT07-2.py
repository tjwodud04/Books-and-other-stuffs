#06
import turtle
import math

width = 200
diagonal = math.sqrt(width**2 + width**2)

turtle.shape('turtle')
turtle.color('blue')
turtle.pensize(5)

for i in range(4):
    turtle.left(90)
    turtle.forward(width)

turtle.left(90+45)
turtle.forward(diagonal)
turtle.right(90)
turtle.forward(diagonal/2)
turtle.right(90)
turtle.forward(diagonal/2)
turtle.right(90)
turtle.forward(diagonal)

turtle.done()

#07
import turtle as t

print('다각형을 그리는 예제입니다.')
var1 = input('변의 수를 입력해주세요? [3-8] ')
var2 = input('한변의 길이를 입력해주세요? [100-200] ')

num_of_side = int(var1)
len_of_side = int(var2)

angle = 360.0 / num_of_side
c_mod = num_of_side % 3
color = 'red' if c_mod==0 else 'green' if c_mod==1 else 'blue'

t.begin_fill()
t.color(color)
t.pensize(5)

for i in range(num_of_side):
    t.forward(len_of_side)
    t.left(angle)

t.end_fill()

t.done()

#08
import turtle

turtle.color('red')
turtle.pensize(10)

for i in range (6):
    for j in range(6):
        turtle.forward(100)
        turtle.left(360/6)

    turtle.forward(100)
    turtle.right(60)

turtle.done()

#09
import turtle as t

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'magenta', 'violet']

for i in range(45):
    t.color(colors[i%len(colors)])
    t.forward(2 + i*5)
    t.left(45)
    t.width(i)

t.done()