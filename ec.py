from tkinter import *
import tkinter
from tkinter import messagebox
root = Tk()
root.title("ELECTRONIC CONFIGURATION")
l1=Label(root,text="This program calculates the ELECTRONIC CONFIGURATION from ATOMIC NUMBER",fg='green')
l1.pack(pady=10)
l2=Label(root,text="Enter the Atomic Number(Z):",fg='black')
l2.pack(pady=5)
e=Entry(root,fg='blue')
e.pack(pady=5)
def printan():
    try:
        z=int(e.get())
        if z in range(1,119):
            import mysql.connector as sqlcon
            import sys
            con=sqlcon.connect(host='localhost',user='root',passwd='cricket@08',database='project')
            cursor=con.cursor()
            cursor.execute('select * from ec where Atomic_No={}'.format(z))
            result=cursor.fetchone()
            l3=Label(root,text='Atomic Noumber: '+str(result[0]),fg='red')
            l3.pack(pady=5)
            l3=Label(root,text='Sytmbol: '+str(result[1]),fg='red')
            l3.pack(pady=5)
            l3=Label(root,text='Element: '+str(result[2]),fg='red')
            l3.pack(pady=5)
            a=str(result[3])
            list=a.split()
            print(list)
            superscript = ["¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹","¹⁰","¹¹","¹²","¹³","¹⁴"]
            for i in range(0,len(list)):
                if i==0:
                    pass
                elif i%2==0:
                    list[i]=superscript[int(list[i])-1]
            s=''
            for i in list:
                s+=i
            l3=Label(root,text='Valence Shell Configuration: '+s,fg='red')
            l3.pack(pady=5)
            l3=Label(root,text='Group Number: '+str(result[4]),fg='red')
            l3.pack(pady=5)
            l3=Label(root,text='Period Noumber: '+str(result[5]),fg='red')
            l3.pack(pady=5)
            l3=Label(root,text='Atomic Mass: '+str(result[6]),fg='red')
            l3.pack(pady=5)
            l3=Label(root,text='Electronegativity: '+str(result[7]),fg='red')
            l3.pack(pady=5)
            con.close()
            sys.exit()
            pass
        elif z not in range(1,119):
             messagebox.showerror(title='Z not in range', message='Enter atomic number between 1-118')
        else:
            messagebox.showerror(title='Z not in range', message='Enter atomic number between 1-118')
    except Exception:
            messagebox.showerror(title='Z not in range', message='Enter atomic number between 1-118')

        
              
button=Button(root,text='Click to Enter the value',command=printan,bg='black',fg='white')
button.pack(pady=5)
root.mainloop()

