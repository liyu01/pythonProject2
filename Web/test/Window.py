#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
import serial.tools.list_ports
from tkinter import ttk

top = Tk()
top.title("串口操作")
top.geometry('650x650+10+10')
menubar = Menu(top)

cmb = ttk.Combobox(top)
cmb.grid()
Texta = Text(top, width="40", height="20", pady=0)
Texta.grid(row=1, column=0, rowspan=10, columnspan=10)
Textb = Text(top, width="40", height="20", pady=0)
Textb.grid(row=1, column=12, rowspan=15, columnspan=10)


# labela = Label(top, text="SERIAL")
# labela.grid()


def get_text():
    t = Texta.get(1.0, END)
    Textb.delete(1.0, END)
    Textb.insert(1.0, t)
    return t


def get_Serial():
    plist = list(serial.tools.list_ports.comports())
    if len(plist) <= 0:
        print("The Serial port can't find!")
    else:
        plist_0 = list(plist[0])
        serialName = plist_0[0]
        serialFd = serial.Serial(serialName, 115200, timeout=60)
        print("check which port was really used >", serialFd.name)
    return serialFd.name


def insert_combobox_Sei():
    cmb['value'] = (get_Serial())
    return


def check_button():
    if CheckVar1.get() == True:
        t = Texta.get(1.0, END)
        Textb.delete(1.0, END)
        Textb.insert(1.0, t)


cmb['value'] = (get_Serial())
button1 = Button(top, text="开始测试", bg="#E6E6FA", activebackground="#F8F8FF", command=insert_combobox_Sei)
button1.grid()
button2 = Button(top, text="结束测试", bg="#E6E6FA", activebackground="#F8F8FF", command=check_button)
button2.grid()
#  复选框 variable为是否选中，get方法，返回TRUE,FALSE
CheckVar1 = IntVar()
C1 = Checkbutton(top, text="转换成16进制", variable=CheckVar1, onvalue=1, offvalue=0, height=2, width=10, command=get_text())
C1.grid()
C1.place()

# 菜单栏
filemenu = Menu(menubar, tearoff=False)
explainmenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="文件", menu=filemenu)
menubar.add_cascade(label="说明", menu=explainmenu)
filemenu.add_command(label="退出", command=top.quit())
filemenu.add_command(label="打开", command=top.quit())
top.config(menu=menubar)
top.mainloop()
