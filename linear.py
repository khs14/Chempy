import turtle
t=turtle.Turtle()
t.penup()
t.goto(0,100)
t.write('Geometry : Linear ',font=('Calibri',28,'bold'))
t.goto(0,50)
t.write("Shape : Linear ",font=('Calibri',28,'bold'))
t.goto(0,-8)
t.write("A")
t.goto(10,0)
t.pendown()
t.forward(50)
t.penup()
t.write("B")
t.goto(-10,0)
t.left(180)
t.pendown()
t.forward(50)
t.write("B")
t.hideturtle()
