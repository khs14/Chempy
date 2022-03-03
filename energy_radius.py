from tkinter import *
import tkinter
from tkinter import messagebox
root = Tk()
root.title("ENERY and RADII")
l1=Label(root,text="This program calculates the ENERGIES and RADII for stationary states in uni-electron species",fg='green')
l1.pack(pady=10)
l2=Label(root,text="Enter the Atomic Number(Z):",fg='black')
l2.pack(pady=5)
e=Entry(root,fg='blue')
e.pack(pady=5)
l2=Label(root,text="Enter the Stationary State(n): ",fg='black')
l2.pack(pady=5)
e2=Entry(root,fg='blue')
e2.pack(pady=5)
def printan():
    try:
        z=int(e.get())
        n=int(e2.get())
        if z in range(1,119) and n>=1:
            E=-2.18*10**(-18)*(z/n)**2
            s=str(f'{E:.3e}')
            energy=s.split(sep='e')
            result=str(energy[0])+" x 10^"+str(energy[1])
            l3=Label(root,text="The energy for stationary state with n = "+str(n)+" and Z = "+str(z)+" is: "+str(result)+" Joules ",fg='blue')
            l3.pack(pady=10)
            R=52.9*((n)**2/z)
            l4=Label(root,text="The radii for stationary state with n = "+str(n)+" and Z = "+str(z)+" is: "+str(R)+" x 10^-12 m",fg='blue')
            l4.pack(pady=10)
            pass
        elif z not in range(1,119):
             messagebox.showerror(title='Z not in range', message='Enter atomic number between 1-118')
        elif n<1:
             messagebox.showerror(title='n not in range', message='Enter Stationary State as a Natural Number')
    except Exception:
        if z not in range(1,119):
             messagebox.showerror(title='Z not in range', message='Enter atomic number between 1-118')
        elif n<1:
             messagebox.showerror(title='n not in range', message='Enter Stationary State as a Natural Number')
        
              
button=Button(root,text='Click to Enter the value',command=printan,bg='black',fg='white')
button.pack(pady=5)
root.mainloop()
