#!/usr/bin/python
# -*- coding: UTF-8 -*-

import calendar
import time


def timetest():
    localtime = time.localtime(time.time())
    print("本地时间为：", localtime)
    # 格式化成2016-03-20 11:45:39形式
    print(time.strftime("%Y-%m-%d %H:%M:%S %p %j", time.localtime()))
    # 格式化成Sat Mar 28 22:24:24 2016形式
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
    # 将格式字符串转换为时间戳
    a = "2017-12-24 11:45:39"
    print(time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S")))
    return


def caltest():
    cal = calendar.month(2017, 12)
    print("一下是2020年10月日历")
    print(cal)


if __name__ == "__main__":
    timetest()
    caltest()
