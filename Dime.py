import Tkinter as tk
#from tkinter import filedialog
import math
#import matplotlib.backends.backend_tkagg

import os
from os import system
import numpy as np
#import Calculate_RoR
import sys

from PyQt4 import QtGui, QtCore 
import xlsxwriter




# declaration of the fields

fields = ('Debts','Income','Mortgage', 'Education', 'Existing_Insurance','Total DB Needed')

 

  
def final_calc(entries):
      
   debt =  float(entries['Debts'].get()) 
   incm = float(entries['Income'].get()) 
   mrtg = float(entries['Mortgage'].get())

   edu = float(entries['Education'].get())
   curr_cov = float(entries['Existing_Insurance'].get())
   incm = incm*10
  
   total_ins = (debt + incm+mrtg+edu)-curr_cov
   
   entries['Total DB Needed'].delete(0,tk.END)
   entries['Total DB Needed'].insert(0, ("%1.2f" % total_ins).strip() )
  
def ResetValues(entries):
     

    float(entries['Debts'].get())
    entries['Debts'].delete(0,tk.END)
    entries['Debts'].insert(0,"0")
    
    float(entries['Income'].get()) 
    entries['Income'].delete(0,tk.END)
    entries['Income'].insert(0,"0")
    
    float(entries['Mortgage'].get())
    entries['Mortgage'].delete(0,tk.END)
    entries['Mortgage'].insert(0,"0")

    float(entries['Education'].get())
    entries['Education'].delete(0,tk.END)
    entries['Education'].insert(0,"0")
    
    float(entries['Existing_Insurance'].get())
    entries['Existing_Insurance'].delete(0,tk.END)
    entries['Existing_Insurance'].insert(0,"0") 
    
    float(entries['Total DB Needed'].get())
    entries['Total DB Needed'].delete(0,tk.END)
    entries['Total DB Needed'].insert(0,"0")

def SaveFile(entries):

    #Lets point  the Dime xlsx file into tmp folder
    # if  dir not  existing, we create

    file_path="c:\\tmp\\Dime.xlsx"
    dir_path= os.path.dirname(file_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
     


# Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()
    
    # Widen the first column to make the text clearer.
    worksheet.set_column('F:A', 18)
    
    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})
    
    # Write some simple text.
    worksheet.write('A1', 'Debts', bold)
    worksheet.write('B1','Income',bold)
    worksheet.write('C1','Mortgage',bold)
    worksheet.write('D1','Education', bold)
    worksheet.write('E1','Existing Insurance', bold)
    worksheet.write('F1','Total Ins. needed', bold)
    
    for i in entries:
    # Write some numbers, with row/column notation.
        worksheet.write(1, 0, float(entries['Debts'].get()) )
        worksheet.write(1, 1, float(entries['Income'].get()))
        worksheet.write(1, 2, float(entries['Mortgage'].get()))
        worksheet.write(1, 3, float(entries['Education'].get()))
        worksheet.write(1, 4, float(entries['Existing_Insurance'].get()))
        worksheet.write(1, 5, float(entries['Total DB Needed'].get()))

# Insert an image.
    worksheet.insert_image('G5', 'life-insurance.jpg')

    workbook.close()
# Lets  set our folder to store the xlsx files

    
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


    
def main():
   
   root = tk.Tk()
   root.title('Can I Retire?')
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: tk.fetch(e)))   
   b1 = tk.Button(root, text='Calculate',
   command=(lambda e=ents: final_calc(e)))
   b1.pack(side=tk.LEFT, padx=5, pady=5)
   
   b7 = tk.Button(root, text='Reset', command =(lambda e=ents:ResetValues(e)))
   b7.pack(side=tk.LEFT, padx=5, pady=5)
   
   b8 = tk.Button(root, text='Save to File', command=(lambda e=ents:SaveFile(e)))
   b8.pack(side= tk.RIGHT, padx=5, pady=5)   
   
  
  
   root.mainloop()
if __name__ == '__main__':
     main()
