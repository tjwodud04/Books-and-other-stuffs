#01
import turtle

in_color = input('원의 색깔을 입력하세요. (R/G/B/etc)  ')
is_filled = input('원의 색깔로 채우겠습니까? (Yes/No)  ')

if in_color == 'R' or in_color == 'r':
    color = 'red'
elif in_color == 'G' or in_color == 'g':
    color = 'green'
elif in_color == 'B' or in_color == 'b':
    color = 'blue'
else:
    color = 'black'

turtle.begin_fill()

turtle.color(color)
turtle.pensize(10)
turtle.circle(100)

if is_filled == 'Y' or is_filled == 'y':
    turtle.end_fill()
else:
    pass

turtle.done()

#02
import turtle as t

num_circle = 30
radius = 180

t.bgcolor("blue")
t.color("yellow")
t.speed(0)

for _ in range(num_circle):
    t.circle(radius)
    t.left(360/num_circle)

t.done()

#03
import turtle as t

t.pensize(3)
t.color('red')

for i in range(10):
    t.forward(15)
    t.penup()
    t.forward(15)
    t.pendown()

t.done()

#04
import turtle as t

print('다각형을 그리는 예제입니다.')
var1 = input('변의 수를 입력해주세요? [3-8] ')
var2 = input('한변의 길이를 입력해주세요? [100-200] ')
# var2 = str(150)

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