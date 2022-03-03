import turtle
t=turtle.Turtle()
t.speed(0)
t.penup()
t.setpos(-50,200)

t.write('2p'+'ₓ',font=('Calibri',20,'bold'))

t.color('black')
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

t.color('red')

t.penup()
t.goto(0.24,100)
t.right(110)
t.write("Z",font='32')
t.pendown()
t.forward(300)
t.write("Z",font='32')

t.penup()
t.goto(200,1.26)
t.right(88)
t.write("y",font='32')
t.pendown()
t.forward(300)
t.write("y",font='32')
t.color('white')
t.penup()
t.goto(0.24,1.26)
t.left(45)
t.pendown()
t.forward(300)
t.write("x",font='32')

t.penup()
t.goto(0.24,1.26)
t.left(180)
t.pendown()
t.forward(300)
t.write("x",font='32')

t.hideturtle()
