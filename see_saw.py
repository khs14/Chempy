import turtle
t=turtle.Turtle()
t.penup()
t.goto(0,200)
t.write('Geometry : Trigonal bi-pyramidal ',font=('Calibri',24,'bold'))
t.goto(0,150)
t.write("Shape : See saw ",font=('Calibri',24,'bold'))
t.goto(0,100)
t.write("Molecule type : AB"+ u'\u2084'+'E',font=('Calibri',24,'bold'))
t.goto(0,0)
t.write("A")
t.left(45)
t.goto(1.5,0)
t.pendown()
t.forward(50)
t.write('B')
t.penup()
t.goto(1.5,0)
t.left(90)
t.left(45)
t.pendown()
t.forward(50)
t.color('red')
t.penup()
t.goto(-55,-8)
t.write(':',font=('Calibri',32,'bold'))
t.color('black')
t.goto(0,-1.5)
t.left(90)
t.pendown()
t.forward(50)
t.write('B')
t.penup()
t.goto(1.5,0)
t.left(45)
t.pendown()
t.forward(50)
t.write("B")
t.penup()
t.goto(1.5,0)
t.left(90+45)
t.pendown()
t.forward(50)
t.write("B")
t.hideturtle()