import turtle
t=turtle.Turtle()
t.penup()
t.goto(150,200)
t.write("1s",font='64')
t.color('blue')

t.begin_fill()
t.goto(0,0)
t.begin_fill()
t.pendown()
t.circle(100)
t.end_fill()
t.color('red')
t.penup()
t.goto(-150,100)
t.pendown()
t.write('x',font='32')
t.forward(400)
t.write('x',font='32')
t.penup()
t.goto(0,-50)
t.left(90)
t.pendown()
t.write(' z',font='32')
t.forward(400)
t.write(' z',font='32')
t.hideturtle()
