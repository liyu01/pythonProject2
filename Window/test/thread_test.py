#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 多线程实例
import time
import threading


def mark():
    # 暂停3秒
    time.sleep(3)
    print("Mark的帅，远近闻")


if __name__ == "__main__":
    print("程序开始执行了")
    # 定义子线程
    t = threading.Thread(target=mark)
    # 启动子线程
    t.start()
    print("单线程程序到这里主线程就会结束了，多线程呢，看看吧")
