#!/usr/bin/python
# -*- coding: UTF-8 -*-


from tkinter import *

top = Tk()
top.title("串口操作")
top.geometry('650x650+10+10')
menubar = Menu(top)
Texta = Text(top, width="40", height="20", pady=0)
Texta.grid(row=1, column=0, rowspan=10, columnspan=10)
Textb = Text(top, width="40", height="20", pady=0)
Textb.grid(row=1, column=12, rowspan=15, columnspan=10)
labela = Label(top, text="Hello boy")
labela.grid()


def get_text():
    t = Texta.get(1.0, END)
    Textb.delete(1.0, END)
    Textb.insert(1.0, t)
    return t


def get_serial():
    return


button1 = Button(top, text="开始测试", bg="#E6E6FA", activebackground="#F8F8FF", command=get_text)
button1.grid()
#  复选框
CheckVar1 = IntVar()
C1 = Checkbutton(top, text="啥也不是", variable=CheckVar1, onvalue=1, offvalue=0, height=2, width=10)
C1.grid()

# 菜单栏
filemenu = Menu(menubar, tearoff=False)
explainmenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="文件", menu=filemenu)
menubar.add_cascade(label="说明", menu=explainmenu)
filemenu.add_command(label="退出", command=top.quit())
filemenu.add_command(label="打开", command=top.quit())
top.config(menu=menubar)
top.mainloop()
