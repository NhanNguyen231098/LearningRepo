import turtle

a = int(input('Nhập vào số hình: '))
angle = 360/a

t = turtle.Turtle()
t.speed(0)

while a > 0:
    loop = 0
    while loop < 2:
        i = 0
        while i < 90:
            t.fd(1)
            t.rt(1)
            i += 1
        i = 0
        while i < 90:
            t.fd(1/2)
            t.rt(1)
            i += 1
        loop += 1
    t.lt(angle)
    a -= 1