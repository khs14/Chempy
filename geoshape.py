from tkinter import *
import tkinter
from tkinter import messagebox
root = Tk()
root.title("Geometry and Shape")
l1=Label(root,text="This program draws Geometry and Shape by taking number of Bond pair and Lone pair electons as input",fg='green')
l1.pack(pady=10)
l2=Label(root,text="Enter the number of BOND PAIR Electrons:",fg='black')
l2.pack(pady=5)
e=Entry(root,fg='blue')
e.pack(pady=5)
l2=Label(root,text="Enter the number of LONE PAIR Electrons: ",fg='black')
l2.pack(pady=5)
e2=Entry(root,fg='blue')
e2.pack(pady=5)
def printan():
    try:
        bp=int(e.get())
        lp=int(e2.get())
        if bp==2 and lp==1:
            import bent
        elif bp==3 and lp==1:
            import Trigonal_pyramidal
        elif bp==2 and lp==2:
            import bent2
        elif bp==4 and lp==1:
            import see_saw
        elif bp==3 and lp==2:
            import tshape
        elif bp==5 and lp==1:
            import squarepyra
        elif bp==4 and lp==4:
            import squarepla
        elif bp not in range(2,6):
             messagebox.showerror(title='Number of Bond Pair electrons NOT IN Range', message='Enter Bond Pair electrons between 2-5')
        elif lp>3:
             messagebox.showerror(title='Number of Lone Pair electrons NOT IN Range', message='Enter Lone Pair electrons between 1-2')
    except Exception:
        if bp not in range(2,6):
             messagebox.showerror(title='Number of Bond Pair electrons NOT IN Range', message='Enter Bond Pair electrons between 2-5')
        elif lp>3:
             messagebox.showerror(title='Number of Lone Pair electrons NOT IN Range', message='Enter Lone Pair electrons between 1-2')

button=Button(root,text='Click to Enter the value',command=printan,bg='black',fg='white')
button.pack(pady=5)
root.mainloop()
