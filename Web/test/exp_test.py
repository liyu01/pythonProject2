#!/usr/bin/python
# -*- coding: UTF-8 -*-

def use_finally(x, y):
    try:
        print(x / y)
    except ZeroDivisionError:
        print('some bad thing happed:division by zero')
    finally:
        print('No matter what happened,I will show in front of you')


if __name__ == "__main__":
    use_finally(2, 0)
