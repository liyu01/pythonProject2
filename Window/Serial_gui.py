#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import ttk
import threading
import os
import time
import serial
import yaml
import serial.tools.list_ports


class MY_GUI():
    def __init__(self, tk):
        self.tk = tk

    # 设置窗口
    def set_init_window(self):
        self.var = BooleanVar()
        # 标签控件
        Label(self.tk, text="串口号:").grid(row=0, sticky=E)
        Label(self.tk, text="波特率:").grid(row=2, sticky=E)
        Label(self.tk, text="实时日志").grid(row=5, sticky=E)
        Label(self.tk, text="次数:").grid(row=0, column=4, sticky=E)

        self.Index = Entry(self.tk, width=6)
        self.Index.grid(row=0, column=6)
        self.Index.insert(0, 6)
        # 输入控件
        self.cmb = ttk.Combobox(self.tk)
        self.cmb.grid(row=0, column=1, padx=10, pady=10, sticky=W)
        self.cmb1 = ttk.Combobox(self.tk)
        self.cmb1.grid(row=2, column=1, padx=10, pady=10, sticky=W)
        self.cmb1['values'] = ('115200', '9600')
        self.cmb1.current(0)
        # 多选框插件
        self.button = Checkbutton(self.tk, text="重启", variable=self.var)
        self.button.grid(row=3, columnspan=2, sticky=W)
        # 插入展示框
        self.text1 = Text(self.tk, width=80, height=30)
        self.text1.grid(row=6, columnspan=16)
        # 按钮控件
        self.button1 = Button(self.tk, text="开始测试", command=lambda: self.thread_it(self.start))
        self.button1.grid(row=0, column=2)
        self.port = self.get_port()
        # 获取的串口号放入cmb
        self.cmb['value'] = self.port

    def get_port(self):
        # 获取串口列表信息
        self.port_list = list(serial.tools.list_ports.comports())
        # 定义空list 存放串口号
        self.comlist = []
        # 遍历port_list 存放到comlist
        for i in range(0, len(self.port_list)):
            self.comlist.append(self.port_list[i][0])
        return self.comlist

    def start(self):
        # 选择重启复选框
        check = self.var.get()
        if check:
            # button状态不可点击
            self.button1['state'] = DISABLED
            d = self.read_yml()
            com = self.cmb.get()
            index = int(self.Index.get())
            bps = self.cmb1.get()
            if com == "":
                self.text1.insert(1.0, "请选择串口号\n")
            else:
                self.text1.delete(1.0, END)
                com_sort = self.cmb.get()
                self.text1.insert(1.0, "程序运行\n")
                com1 = self.serial_set(com_sort, bps)
                self.log_Read(com=com1, order=d[2]["order"], expect=d[4]["expect"], count=index)
                self.button1['state'] = NORMAL
                return
        else:
            self.text1.insert(1.0, "选择程序\n")

    def thread_it(self, func, *args):
        '''将函数打包进线程'''
        # 创建
        t = threading.Thread(target=func, args=args)
        # 守护 !!!
        t.setDaemon(True)
        # 启动
        t.start()
        # 阻塞--卡死界面！
        # t.join()

    def serial_set(self, com, bps):
        #  串口设置

        bamp = serial.Serial(com, bps, timeout=10)
        flag = bamp.is_open
        if flag:
            return bamp
        else:
            print("串口无法打开")

    def read_yml(self):
        # 文件是否存在
        if not os.path.isfile("./date/ser.yml"):
            raise FileNotFoundError("文件路径不存在， 请检查路劲是否正确： %s" % "./date/ser.yml")
        else:
            # open 方法打开直接读出来
            f = open("./date/ser.yml", 'r', encoding='utf-8')
            cfg = f.read()
            # 将其转化为字典形式
            d = yaml.load(cfg, Loader=yaml.FullLoader)
            # print("读取的测试文件数据： %s" % d)
            return d

    def script_write(self, order, com):
        #  串口指令操作
        if order == None:
            com.write("\n".encode())
        else:
            com.write("\n".encode())
            com.write(order.encode())
            com.write("\n".encode())
        time.sleep(3)
        return None

    def log_Read(self, order, com, expect, count):
        """串口读取"""
        # print(com)
        t = self.make_Txt()
        # 控制重启次数
        counts = count + 1
        for i in range(1, counts):
            for y in order:
                self.script_write(y, com)
            self.text1.insert("end", "第" + str(i) + "次重启\n")
            self.Date_txtpath(t, f"重启第 {i} 次" + "\n")
            while True:
                #  按行读取串口数据
                date = com.readline()
                strdate = str(date)
                self.Date_txtpath(t, strdate + "\n")
                for x in expect:
                    if x in strdate:
                        self.text1.insert("end", strdate + "\n")
                if strdate == "b''":
                    self.text1.insert("end", "退出\n")
                    break
        return None

    def make_Txt(self):
        # 获取时间戳转换时间
        now = int(time.time())
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H-%M-%S", timeArray)
        # print(otherStyleTime)
        fname1 = otherStyleTime + ".txt"
        #  拼接log地址
        pathtxt = "./log" + "/" + fname1
        t = open(pathtxt, 'w')
        return t

    def Date_txtpath(self, t, date):
        # 数据输入
        t.write(date)
        return None

if __name__ == '__main__':
    tk = Tk()  # 实例化出一个父窗口
    tk.title("串口测试工具")
    ZMJ_PORTAL = MY_GUI(tk)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    tk.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
