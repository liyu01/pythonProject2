#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)  # 创建画布
canvas.pack()


def moverectangle(event):
    if event.keysym == "Up":  # 获取你点击的键盘内容
        canvas.move(1, 0, -5)
        print(event.keysym)

    elif event.keysym == "Down":
        canvas.move(1, 0, 5)
        print(event.keysym)

    elif event.keysym == "Left":
        canvas.move(1, -5, 0)
        print(event.keysym)

    elif event.keysym == "Right":
        canvas.move(1, 5, 0)
        print(event.keysym)


canvas.create_rectangle(10, 10, 50, 50, fill="yellow")  # 画出方块
canvas.create_rectangle(10, 10, 50, 50, fill="red")  # 画出方块

canvas.bind_all("<KeyPress-Up>", moverectangle)  # 通过键盘，触发函数
canvas.bind_all("<KeyPress-Down>", moverectangle)
canvas.bind_all("<KeyPress-Left>", moverectangle)
canvas.bind_all("<KeyPress-Right>", moverectangle)

mainloop()
