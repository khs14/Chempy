import turtle
t=turtle.Turtle()
t.penup()
t.goto(0,200)
t.write('Geometry : Octahedral ',font=('Calibri',28,'bold'))
t.goto(0,150)
t.write("Shape : Square planer",font=('Calibri',24,'bold'))
t.goto(0,100)
t.write("Molecule type : AB"+ u'\u2084'+'E'+u'\u2082',font=('Calibri',24,'bold'))
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
t.goto(0,-1.5)
t.left(90)
t.forward(50)
t.penup()
t.color('red')
t.goto(0,-60)
t.pendown()
t.write('..',font=('Calibri',32,'bold'))
t.color("black")
t.penup()
t.goto(1.5,0)
t.left(45)
t.pendown()
t.forward(50)
t.write("B")
t.penup()
t.goto(0,1.5)
t.left(45+90)
t.pendown()
t.forward(50)
t.color('red')
t.write('..',font=('Calibri',32,'bold'))
t.color("black")
t.penup()
t.goto(-1.5,0)
t.left(45)
t.pendown()
t.forward(50)
t.write("B")
t.penup()
t.goto(-1.5,0)
t.left(90)
t.pendown()
t.forward(50)
t.write("B")
t.hideturtle()
