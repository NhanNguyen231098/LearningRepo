import turtle

a = int(input('Nhập vào quãng đường: '))

t = turtle.Turtle()
t.speed(0)
d = 0.2
i = 0
total = 0
while True:
    if i == 180:
        i = 0
        d += 0.2
    t.fd(d)
    t.rt(1)
    i += 1
    total += d
    if total >= a:
        break