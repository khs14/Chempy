import turtle
t=turtle.Turtle()
t.speed(0)
t.penup()
t.setpos(-50,200)
t.write('3dₓ²₋ᵧ²',font=('Calibri',28,'bold'))
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
t.goto(0.24,1.26)
t.left(45)
t.pendown()
t.forward(300)
t.write("y",font='32')

t.penup()
t.goto(0.24,1.26)
t.left(180)
t.pendown()
t.forward(300)
t.write("y",font='32')

t.penup()
t.goto(0.24,1.26)
t.left(135-40)
t.pendown()
t.forward(300)
t.write("y",font='32')

t.penup()
t.goto(0.24,1.26)
t.left(180)
t.pendown()
t.forward(300)
t.write("y",font='32')
t.hideturtle()

