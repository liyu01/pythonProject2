#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *

app = Tk()
v1 = BooleanVar()
v2 = BooleanVar()

c1 = Checkbutton(text='复选框1', variable=v1)
c2 = Checkbutton(text='复选框2', variable=v2)

c1.pack()
c2.pack()


def check_status():
    print(v1.get())
    print(v2.get())


btn = Button(text='获取复选框中的内容', command=check_status)
btn.pack()
app.mainloop()
