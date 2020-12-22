#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import ttk
import serial.tools.list_ports

from serialLog.SerialCap import SerialSet


def get_Serial():
    plist = list(serial.tools.list_ports.comports())
    if len(plist) <= 0:
        print("The Serial port can't find!")
    else:
        plist_0 = list(plist[0])
        serialName = plist_0[0]
        serialFd = serial.Serial(serialName, 115200, timeout=60)
        # print("check which port was really used >", serialFd.name)
        cmb['value'] = (serialFd.name)


def start():
    d = SerialSet().read_yml()
    com1 = SerialSet().ser_set(cmb.get(), bps=d[1]["bps"])
    SerialSet().log_Read(com=com1, order=d[2]["order"], expect=d[4]["expect"], count=d[3]["count"])
    return


tk = Tk()
var = IntVar()
tk.title("串口操作")
tk.geometry('650x650+10+10')

# 标签控件，显示文本和位图，展示在第一行
Label(tk, text="串口号").grid(row=0, sticky=E)  # 靠右
Label(tk, text="事实日志").grid(row=5, sticky=E)  # 靠右

# 输入控件
cmb = ttk.Combobox(tk)
cmb.grid(row=0, column=1, padx=10, pady=10)

# 多选框插件
button = Checkbutton(tk, text="重启", variable=var)
button.grid(row=3, columnspan=2, sticky=W)
# 插入展示框
text1 = Text(tk, width=50, height=30, state='disabled')
text1.grid(row=6, columnspan=6)
# 插入图片
# photo=PhotoImage(file="python_logo.gif")
# label=Label(image=photo)
# label.grid(row=0,column=2,rowspan=2,columnspan=2,
#            sticky=W+E+N+S, padx=5, pady=5)#合并两行，两列，居中，四周外延5个长度

# 按钮控件
button1 = Button(tk, text="开始测试", command=start)
button1.grid(row=0, column=2)

get_Serial()
# 主事件循环
mainloop()
