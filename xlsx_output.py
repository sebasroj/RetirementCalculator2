# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:33:16 2015

@author: info2070
"""
import xlsxwriter


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
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


# Write some numbers, with row/column notation.
worksheet.write(1, 0, )
worksheet.write(3, 0, 123.456)

# Insert an image.
#worksheet.insert_image('B5', 'logo.png')

workbook.close()

