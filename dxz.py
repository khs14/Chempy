import turtle
t=turtle.Turtle()
t.speed(0)
t.penup()
t.setpos(-50,200)
t.write('3dₓ₂',font=('Calibri',14,'bold'))
t.color('orange')
t.goto(0.24,1.26)
t.pendown()
t.begin_fill()
for i in range(200):
    t.forward(3)
    t.left(0.2+(i/100))
for i in range(100):
    t.forward(3)
    t.left(0.2+(i/1000))
for i in range(200):
    t.forward(3)
    t.right(0.2+(i/100))
for i in range(56):
    t.forward(5)
    t.right(0.1+(i/1000))
t.end_fill()

t.color('blue')
t.goto(0.24,1.26)
t.left(180)
t.pendown()
t.begin_fill()
for i in range(200):
    t.forward(3)
    t.right(0.2+(i/100))
for i in range(100):
    t.forward(3)
    t.right(0.2+(i/1000))
for i in range(200):
    t.forward(3)
    t.left(0.2+(i/100))
for i in range(56):
    t.forward(5)
    t.left(0.1+(i/1000))
t.end_fill()

t.color('red')

t.penup()
t.goto(-0.37,-100)
t.right(90)
t.write("Z",font='32')
t.pendown()
t.forward(450)
t.write("Z",font='32')



t.penup()
t.goto(200,2.38)
t.left(90)
t.write("x",font='32')
t.pendown()
t.forward(250)
t.write("x",font='32')
t.hideturtle()

