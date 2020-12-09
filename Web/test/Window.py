#!/usr/bin/python
# -*- coding: UTF-8 -*-


import tkinter


def get_text():
    print(Textb.get())


top = tkinter.Tk()
menubar = tkinter.Menu(top)
listb = tkinter.Listbox(top, width="60", height="20")  # 创建两个列表组件
Textb = tkinter.Text(top, width="20", height="20")
listb1 = tkinter.Listbox(top, width="60", height="20")  # 创建两个列表组件
button1 = tkinter.Button(top, text="点我", bg="red", activebackground="yellow", menubar=get_text)
CheckVar1 = tkinter.IntVar()
C1 = tkinter.Checkbutton(listb, text="RUNOOB", variable=CheckVar1, \
                         onvalue=1, offvalue=0, height=2, \
                         width=10)
filemenu = tkinter.Menu(menubar, tearoff=False)
explainmenu = tkinter.Menu(menubar, tearoff=False)

listb.pack()  # 将小部件放置到主窗口中
listb1.pack()  # 将小部件放置到主窗口中
button1.pack()
Textb.pack()
C1.pack()
menubar.add_cascade(label="文件", menu=filemenu)
menubar.add_cascade(label="说明", menu=explainmenu)
filemenu.add_command(label="退出", command=top.quit())
filemenu.add_command(label="打开", command=top.quit())
top.config(menu=menubar)
top.mainloop()
