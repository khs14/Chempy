from tkinter import *
from PIL import ImageTk,Image
import cv2
root = Tk()
root.title('Chemistry') 
menubar = Menu(root)
i=ImageTk.PhotoImage(Image.open(r'Project pic.jpeg'))
l=Label(image=i)
l.pack()

def anion():
    import anion

def titration():
    path = r'Titration 1.JPG'
    img = cv2.imread(path)
    cv2.imshow('TITRATION', img)
    
def E_R():
    import energy_radius

def ec():
    import ec

def cation():
    import cationmenu

def geoshape():
    import geoshape

def atorbital():
    import orbital_menu

def lin():
    import linear

def tripla():
    import Trigonal_planar
atomic = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Atomic', menu =atomic) 
atomic.add_command(label ='Electronic Configuration',command = ec)
atomic.add_separator()
atomic.add_command(label ='Energies and Radius', command = E_R) 
atomic.add_separator() 
atomic.add_command(label ='Exit', command = root.destroy) 


d2= Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Structure', menu = d2)
d2.add_command(label ='Geomerty and Shape', command = geoshape)
d2.add_separator()
d2.add_command(label ='Linear', command =lin)
d2.add_separator()
d2.add_command(label ='Trigonal Planar', command =tripla)
d2.add_separator()
d2.add_command(label ='Atomic Orbitals', command = atorbital)
d2.add_separator()
d2.add_command(label ='Exit', command = root.destroy) 
  

chemical_reaction = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Practical', menu = chemical_reaction) 
chemical_reaction.add_command(label ='Cation', command = cation)
chemical_reaction.add_separator()
chemical_reaction.add_command(label ='Anion', command = anion) 
chemical_reaction.add_separator() 
chemical_reaction.add_command(label ='Titration', command = titration)
chemical_reaction.add_separator()
chemical_reaction.add_command(label ='Exit', command = root.destroy) 
root.config(menu = menubar)
