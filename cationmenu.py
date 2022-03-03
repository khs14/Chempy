from tkinter import *
from PIL import ImageTk,Image
root2 = Tk() 
root2.title('Cation')
menubar = Menu(root2)
root2.geometry("500x20")
def nh4():
    import nh4
def pb():
    import pb
def cu():
    import cu
def al():
    import al
def fe():
    import fe
def zn():
    import zn
def mn():
    import mn
def ba():
    import ba
def sr():
    import sr
def ca():
    import ca
def mg():
    import mg
def Flowchart():
    import prac 

group0=Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Group 0', menu =group0) 
group0.add_command(label ='NH'+u'\u2084'+u'\u207A', command = nh4)
group0.add_separator()
group0.add_command(label ='Exit', command = root2.destroy) 
  

group1= Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Group 1', menu = group1)
group1.add_command(label ='Pb'+u'\u00B2'+u'\u207A', command = pb)
group1.add_separator()
group1.add_command(label ='Exit', command = root2.destroy) 
  
group2= Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Group 2', menu = group2)
group2.add_command(label ='Cu'+u'\u00B2'+u'\u207A', command = cu)
group2.add_separator()
group2.add_command(label ='Exit', command = root2.destroy) 
  

group3= Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Group 3', menu = group3)
group3.add_command(label ='Al'+u'\u00B3'+u'\u207A', command = al)
group3.add_separator()
group3.add_command(label ='Fe'+u'\u00B3'+u'\u207A', command = fe)
group3.add_separator()
group3.add_command(label ='Exit', command = root2.destroy) 
  

group4= Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Group 4', menu = group4)
group4.add_command(label ='Zn'+u'\u00B2'+u'\u207A', command = zn)
group4.add_separator()
group4.add_command(label ='Mn'+u'\u00B2'+u'\u207A', command = mn)
group4.add_separator()
group4.add_command(label ='Exit', command = root2.destroy) 
  

group5= Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Group 5', menu = group5)
group5.add_command(label ='Ba'+u'\u00B2'+u'\u207A', command = ba)
group5.add_separator()
group5.add_command(label ='Sr'+u'\u00B2'+u'\u207A', command = sr)
group5.add_separator()
group5.add_command(label ='Ca'+u'\u00B2'+u'\u207A', command = ca)
group5.add_separator()
group5.add_command(label ='Exit', command = root2.destroy) 

group6= Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Group 6', menu = group6)
group6.add_command(label ='Mg'+u'\u00B2'+u'\u207A', command = mg)
group6.add_separator()
group6.add_command(label ='Exit', command = root2.destroy) 

d6= Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Flowchart', menu = d6)
d6.add_command(label ='Flowchart', command = Flowchart)
root2.config(menu = menubar)
root2.mainloop()
