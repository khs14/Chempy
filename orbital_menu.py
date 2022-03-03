from tkinter import * 
root = Tk() 
root.title('Orbitals') 
root.geometry("500x20")
menubar = Menu(root) 
def s():
    import s
def pz():
    import pz
def px():
    import px
def py():
    import py
def dz2():
    import dz2
def dxz():
    import dxz
def dx_y():
    import dx_y
def dxy():
    import dxy
def dyz():
    import dyz
group0=Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='s orbital', menu =group0) 
group0.add_command(label ='1s', command = s)
group0.add_separator()
group0.add_command(label ='Exit', command = root.destroy) 
  

group1= Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='p orbital', menu = group1)
group1.add_command(label ='2p₂', command = pz)
group1.add_separator()
group1.add_command(label ='2pᵧ', command = py)
group1.add_separator()
group1.add_command(label ='2pₓ', command = px)
group1.add_separator()
group1.add_command(label ='Exit', command = root.destroy) 
  
group5= Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='d orbital', menu = group5)
group5.add_command(label ='3dₓ₂', command =dxz )
group5.add_separator()
group5.add_command(label ='3dₓ²₋ᵧ²', command =dx_y )
group5.add_separator()
group5.add_command(label ='3dₓᵧ', command =dxy )
group5.add_separator()
group5.add_command(label ='3dᵧ₂', command =dyz )
group5.add_separator()
group5.add_command(label ='Exit', command = root.destroy) 

root.config(menu = menubar)
root.mainloop()
