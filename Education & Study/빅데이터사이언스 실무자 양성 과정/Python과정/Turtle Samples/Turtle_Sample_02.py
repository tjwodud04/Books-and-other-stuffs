import turtle

#01
turtle.pensize(10)

input('엔터를 치면 사각형을 그립니다.')

turtle.color("red")
turtle.forward(200)

turtle.left(90)
turtle.forward(200)

turtle.left(90)
turtle.forward(200)

turtle.left(90)
turtle.forward(200)

turtle.done()

#02
input('엔터를 치면 빨간색 삼각형을 그립니다.')

turtle.color("green")

turtle.right(30)
turtle.forward(300)

turtle.left(120)
turtle.forward(300)

turtle.left(120)
turtle.forward(300)

turtle.done()

#03
input('엔터를 치면 파란색 굵은 원을 그립니다.')

turtle.right(30)
turtle.color("blue")
turtle.circle(200)

turtle.done()

#04
import turtle

size  = input('사각형의 크기를 입력하세요.[100~300] ')
color = input('선의 색깔을 입력하세요.[red / green / blue]  ')
thick = input('펜의 굵기를 입력하세요.[1~30]   ')

angle = 90
thick = int(thick)
size  = int(size)

turtle.color(color)
turtle.pensize(thick)

turtle.left(angle)
turtle.forward(size)

turtle.left(angle)
turtle.forward(size)

turtle.left(angle)
turtle.forward(size)

turtle.left(angle)
turtle.forward(size)

turtle.done()