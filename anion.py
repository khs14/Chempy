from tkinter import *
from anion_functions import *
from PIL import ImageTk,Image
root1 = Tk()
root1.title('Anion')
menubar = Menu(root1)
root1.geometry("300x20")

d3= Menu(menubar, tearoff = 0)

menubar.add_cascade(label ='Category 1', menu = d3)
d3.add_command(label ='Preliminary Test', command = PT1)
d3.add_separator()
d3.add_command(label ='CO₃²⁻', command = CO32_)
d3.add_separator()
d3.add_command(label ='S²⁻', command = S2_)
d3.add_separator()
d3.add_command(label ='SO₃²⁻', command = SO32_)
d3.add_separator()
d3.add_command(label ='NO₂⁻', command = NO2_)
d3.add_separator()
d3.add_command(label ='CH₃COO⁻', command = CH3COO_ )
d3.add_separator()
d3.add_command(label ='Exit', command = root1.destroy)

d4= Menu(menubar, tearoff = 0)

menubar.add_cascade(label ='Category 2', menu = d4)
d4.add_command(label ='Preliminary Test', command = PT2)
d4.add_separator()
d4.add_command(label ='Cl⁻', command = Cl_)
d4.add_separator()
d4.add_command(label =' Br⁻', command = Br_)
d4.add_separator()
d4.add_command(label ='I⁻', command = I_)
d4.add_separator()
d4.add_command(label ='NO₃⁻', command = NO3_)
d4.add_separator()
d4.add_command(label ='Exit', command = root1.destroy)

d5= Menu(menubar, tearoff = 0)

menubar.add_cascade(label ='Category 3', menu = d5)
d5.add_command(label ='Preliminary Test', command = PT3)
d5.add_separator()
d5.add_command(label ='SO₄²⁻', command = SO42_)
d5.add_separator()
d5.add_command(label =' PO₄³⁻', command = PO43_)
d5.add_separator()
d5.add_command(label ='Exit', command = root1.destroy)

d6= Menu(menubar, tearoff = 0)

menubar.add_cascade(label ='Flowchart', menu = d6)
d6.add_command(label ='Flowchart', command = Flowchart)
root1.config(menu = menubar)
root1.mainloop()
