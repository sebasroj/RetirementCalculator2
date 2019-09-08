import Tkinter as tk
import tkMessageBox
#from tkinter import filedialog
import matplotlib
import math
#import matplotlib.backends.backend_tkagg
import matplotlib.backends._tkagg
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
plt.ion()
import os
from os import system
import numpy as np
#import Calculate_RoR
import sys
import hilfe
import Dime
from PyQt4.phonon import Phonon 
from PyQt4 import QtGui, QtCore 
import PyQt4.QtCore
import PyQt4.uic
from PyQt4.uic import port_v3
import  logging

# declaration of the fields
fields = ('Name','Age','Retirement Age','Initial Investment', 'Monthly Payments', 'Investment Years','Annual Rate','Total', 'Money Doubles(yrs)')

 
class MyDialog:

    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        
        self.myLabel = tk.Label(top,  height =30, width = 40) 
        self.myLabel.pack(side=tk.LEFT, fill=tk.Y)
    def send(self):
        self.top.destroy()

#def onClick():
#    inputDialog = MyDialog(root)
#    root.wait_window(inputDialog.top)
#    print('Username: ', inputDialog.username)
def About():
# we are loading the  video player script here (hilfe.py)
     
     hilfe.main()
    
#  Useful docs links
def Tradeticket():
   #os.startfile("TradeTicket.pdf")
    tkMessageBox.showinfo("Your Trade ticket","It will open your trade ticket here")
    
    
def Fls():
    #os.startfile("PFS.pdf")
    tkMessageBox.showinfo("Your KYC","It will open  your KYC here")

def dime_calc():
    Dime.main()

def yourName(entries):
    str(entries['Name'].get())

    
def investmenthorizon(entries):
    #bunch of validations !!!

    inv_t =  int(entries['Investment Years'].get())

   # if inv_t == 0:
    # checking for negative age entry
    x = int(entries['Age'].get())
    y = int(entries['Retirement Age'].get())
    if x>100:
        tkMessageBox.showerror("Age Error", " Are you sure that's your actual age??")
        int(entries['Age'].delete(0, tk.END))
        int(entries['Age'].insert(0, 0))
    if  x<0:
        tkMessageBox.showerror("Error","Age cannot be negative")
        int(entries['Age'].delete(0, tk.END))
        int(entries['Age'].insert(0, '0'))
    if y <0:
        tkMessageBox.showerror("Error", "Retirement Age cannot be negative")
        int(entries['Retirement Age'].delete(0, tk.END))
        int(entries['Retirement Age'].insert(0, '0'))


    if (x==0 and y == 0):
        entries['Investment Years'].insert(0, '0')
        inv_t =  int(entries['Investment Years'].get())

    if x>0<100:
            inv_t = y - x
            #inv_t = ("%1.2f" %inv_t).strip()
            entries['Investment Years'].delete(0,tk.END)
            entries['Investment Years'].insert(0,inv_t)
    if x>y:
        tkMessageBox.showerror("hmm something  does not adds up", "You have outlived your planned retirement age")
        entries['Investment Years'].delete(0, tk.END)
        entries['Investment Years'].insert(0, '0')
    # else:
    #
    #         entries['Investment Years'].delete(0,tk.END)
    #         #inv_t = ("%1.2f" %inv_t).strip()
    #         #inv_t =- inv_t
    #
    #         inv_t = int(entries['Investment Years'].get())
    #         entries['Investment Years'].insert(0,inv_t)




def final_balance(entries):

   inv_t =  float(entries['Investment Years'].get())
   base = float(entries['Initial Investment'].get())
   monthly = float(entries['Monthly Payments'].get())

   apr = (float(entries['Annual Rate'].get()) / 100)
   if float(apr>0):
       V = base + base*(1+apr)**inv_t + monthly*(1 + apr)/apr*((1 + apr)**inv_t - 1)
       entries['Total'].delete(0,tk.END)
       entries['Total'].insert(0, ("%1.2f" % V).strip() )
   else:

       V = base + base*(1+apr)**inv_t + monthly*(1 + apr)/apr*((1 + apr)**inv_t - 1)
       entries['Total'].delete(0,tk.END)
       entries['Total'].insert(0, ("%-1.2f" % V).strip() )

       #V = ("%1.2f" % V).strip()

   print("Annual Rate:", apr*100 ,"%")
   #entries['Total'].insert(0, V )

# reseting all values to 0
def reset(entries):

    float(entries['Investment Years'].get())
    entries['Investment Years'].delete(0,tk.END)
    entries['Investment Years'].insert(0,"0")

    float(entries['Initial Investment'].get())
    entries['Initial Investment'].delete(0,tk.END)
    entries['Initial Investment'].insert(0,"0")

    float(entries['Monthly Payments'].get())
    entries['Monthly Payments'].delete(0,tk.END)
    entries['Monthly Payments'].insert(0,"0")

    float(entries['Annual Rate'].get())
    entries['Annual Rate'].delete(0,tk.END)
    entries['Annual Rate'].insert(0,"0")

    float(entries['Money Doubles(yrs)'].get())
    entries['Money Doubles(yrs)'].delete(0,tk.END)
    entries['Money Doubles(yrs)'].insert(0,"0")

    float(entries['Total'].get())
    entries['Total'].delete(0,tk.END)
    entries['Total'].insert(0,"0")

    int(entries['Age'].get())
    entries['Age'].delete(0,tk.END)
    entries['Age'].insert(0,"0")


    int(entries['Retirement Age'].get())
    entries['Retirement Age'].delete(0,tk.END)
    entries['Retirement Age'].insert(0,"0")

# calculate rule 72
def Rule72(entries):
#getting the rate
    apr = float(entries['Annual Rate'].get())
    rl = 72/apr

    rl = ("%1.2f" %rl).strip()
    entries['Money Doubles(yrs)'].delete(0,tk.END)
    entries['Money Doubles(yrs)'].insert(0,rl)

# thisis for showing the results in a graph

def plot(entries):


    tr = np.linspace(0,float(entries['Total'].get()))
    tm = np.linspace(0,float(entries['Investment Years'].get()))

    apr = (float(entries['Annual Rate'].get()) / 100)
    print("Annual Rate:", apr*100 ,"%")

    #fig, ax, ay = plt.subplots()
    plt.plot(tr,tm,'b--')
    plt.title('Projected Retirement Savings')
    plt.xlabel('Savings ($)')
    plt.ylabel('Time (yrs)')

    plt.grid(True)
    plt.draw()
    plt.show()



# to close the app
def stopProg(e):
    
    root.destroy()  
    
    
# Form maker
def makeform(root, fields):
   entries = {}
   for field in fields:
      row = tk.Frame(root)
      lab = tk.Label(row, width=20, text=field+": ", anchor='w')
      ent = tk.Entry(row)
      ent.insert(0,"0")
      row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
      lab.pack(side=tk.LEFT)
      ent.pack(side=tk.RIGHT, expand=tk.NO, fill=tk.X)
      entries[field] = ent
   return entries
    
if __name__ == '__main__':
   root = tk.Tk()
   root.title('Can I Retire?')
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: tk.fetch(e)))   
   b1 = tk.Button(root, text='Show me the money',
          command=(lambda e=ents: final_balance(e)))
   b1.pack(side=tk.LEFT, padx=5, pady=5)
   
   b4 = tk.Button(root,text='Rule 72', command=(lambda e=ents: Rule72(e)))
   b4.pack(side=tk.LEFT, padx=5, pady=5)
   b5 = tk.Button(root,text='Invest  yrs', command=(lambda e=ents: investmenthorizon(e)))
   b5.pack(side=tk.LEFT, padx=5, pady=5)
   
#   mainButton = tk.Button(root, text='Graph', command=onClick)
#   mainButton.pack(side=tk.LEFT, padx=5, pady=5)
   
   graph_button =tk.Button(root, text='Graph display',command=(lambda e=ents:plot(e)))
   graph_button.pack(side=tk.LEFT, padx=5, pady=5)
   
   b7 = tk.Button(root, text='Reset', command =(lambda e=ents:reset(e)))
   b7.pack(side=tk.LEFT, padx=5, pady=5)
   
   
   b6 = tk.Button(root, text='Quit')
   b6.pack(side=tk.RIGHT, padx=5, pady=5)
   b6.bind('<Button-1>', stopProg)
   
   menu = tk.Menu(root)
   root.config(menu=menu)

   helpmenu = tk.Menu(menu)
   menu.add_cascade(label="Help", menu=helpmenu)
   helpmenu.add_command(label="How to..", command=About)
   
   docs = tk.Menu(menu)
   menu.add_cascade(label ="Usefull Docs",menu=docs)
   docs.add_command(label="Trade ticket",command=Tradeticket)
   docs.add_command(label="FLS",command=Fls)
   
   insur = tk.Menu(menu)
   menu.add_cascade(label="Insurance Calc", menu = insur)
   insur.add_command(label="DIME", command=dime_calc)
   
   
#   helpmenu.add_command(label="Calculate RoR", command=RoR)

  
   root.mainloop()
    
