#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter
from tkinter import ttk  # 导入ttk模块，因为下拉菜单控件在ttk中

wuya = tkinter.Tk()
wuya.title("wuya")
wuya.geometry("300x200+10+20")


def get_value():
    print(cmb.get())


# 创建下拉菜单
cmb = ttk.Combobox(wuya)
button = tkinter.Button(wuya, command=get_value, text="获取")
button.pack()
cmb.pack()
# 设置下拉菜单中的值
cmb['value'] = ('上海', '北京', '天津', '广州')

# 设置默认值，即默认下拉框中的内容
cmb.current(2)
# 默认值中的内容为索引，从0开始


wuya.mainloop()
