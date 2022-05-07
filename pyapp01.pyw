# import openpyxl 
import tkinter as tk
import xlsxwriter
# from openpyxl import *
# from tkinter import *


root = tk.Tk()
workbook = xlsxwriter.Workbook("x.xlsx")
# workbook = xlsxwriter.Workbook("a.xlsx")
worksheet = workbook.add_worksheet()
root.geometry("250x250")
worksheet.write(0,0,"name")
worksheet.write(0,1,"user id")
worksheet.write(0,2,"pass")
x=1
def click():
    global x
    i = fname.get()
    j = userid.get()
    k = password.get()
    worksheet.write(x,0,i)
    worksheet.write(x,1,j)
    worksheet.write(x,2,k)
    x+=1
    print(i,j,k)
# name
tk.Label(root,text="Name").grid(column=1,row=1)
fname = tk.Entry(root)
fname.grid(column=2,row=1)
# user id
tk.Label(root,text="UserID").grid(column=1,row=2)
userid = tk.Entry(root)
userid.grid(column=2,row=2)
# password
tk.Label(root,text="PassWord").grid(column=1,row=3)
password = tk.Entry(root)
password.grid(column=2,row=3)
# button
mybutton = tk.Button(root,text="click",command=click)
mybutton.grid(column=2,row=4)


root.mainloop()
workbook.close()