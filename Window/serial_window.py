#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import ttk
import serial.tools.list_ports
import threading
from serialLog.SerialCap import SerialSet


# def get_Serial():
#     plist = list(serial.tools.list_ports.comports())
#     if len(plist) <= 0:
#         print("The Serial port can't find!")
#     else:
#         plist_0 = list(plist[0])
#         serialName = plist_0[0]
#         serialFd = serial.Serial(serialName, 115200, timeout=60)
#         # print("check which port was really used >", serialFd.name)
#         cmb['value'] = (serialFd.name)


def start():
    d = SerialSet().read_yml()
    com = cmb.get()
    bps = cmb1.get()
    if com == "":
        text1.delete(1.0, END)
        text1.insert(1.0, "请选择串口号\n")
    else:
        com1 = SerialSet().ser_set(cmb.get(), bps)
        SerialSet().log_Read(com=com1, order=d[2]["order"], expect=d[4]["expect"], count=d[3]["count"])
        return

def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()


tk = Tk()
var = IntVar()
tk.title("串口操作")
tk.geometry('650x650+10+10')

# 标签控件，显示文本和位图，展示在第一行
Label(tk, text="串口号:").grid(row=0, sticky=E)  # 靠右
Label(tk, text="波特率:").grid(row=2, sticky=E)  # 靠右
Label(tk, text="实时日志").grid(row=5, sticky=E)  # 靠右

# 输入控件
cmb = ttk.Combobox(tk)
cmb.grid(row=0, column=1, padx=10, pady=10, sticky=W)
cmb1 = ttk.Combobox(tk)
cmb1.grid(row=2, column=1, padx=10, pady=10, sticky=W)
cmb1['values'] = ('115200', '9600')
cmb1.current(0)
# 多选框插件
button = Checkbutton(tk, text="重启", variable=var)
button.grid(row=3, columnspan=2, sticky=W)
# 插入展示框
text1 = Text(tk, width=50, height=30)
text1.grid(row=6, columnspan=6)

# 插入图片
# photo=PhotoImage(file="python_logo.gif")
# label=Label(image=photo)
# label.grid(row=0,column=2,rowspan=2,columnspan=2,
#            sticky=W+E+N+S, padx=5, pady=5)#合并两行，两列，居中，四周外延5个长度

# 按钮控件
button1 = Button(tk, text="开始测试", command=lambda: thread_it(start))
button1.grid(row=0, column=2)

# 主事件循环
mainloop()
