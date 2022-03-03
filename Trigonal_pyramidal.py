import turtle
t=turtle.Turtle()
t.penup()
t.goto(0,200)
t.write('Geometry : Tetrahedral ',font=('Calibri',28,'bold'))
t.goto(0,150)
t.write("Shape : Trigonal pyramidal ",font=('Calibri',28,'bold'))
t.goto(0,100)
t.write("Molecule type : AB"+u'\u2083'+'E',font=('Calibri',28,'bold'))
t.goto(0,0)
t.left(90)
t.right(109.5)
t.pendown()
t.forward(50)
t.write("B")
t.penup()
t.goto(0,5)
t.left(109.5)
t.pendown()
t.write('A')
t.forward(50)
t.color('red')
t.write('..',font=('Calibri',32,'bold'))
t.penup()
t.goto(0,0)
t.left(109.5)
t.pendown()
t.color('black')
t.forward(50)
t.write("B")
t.penup()
t.goto(0,0)
t.left(90)
t.pendown()
t.forward(50)
t.write("B")
t.hideturtle()
