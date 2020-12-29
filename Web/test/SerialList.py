#!/usr/bin/python
# -*- coding: UTF-8 -*-
import serial
import serial.tools.list_ports

# plist = list(serial.tools.list_ports.comports())
#
# if len(plist) <= 0:
#     print("The Serial port can't find!")
# else:
#     plist_0 = list(plist[0])
#     serialName = plist_0[0]
#     print(serialName)
#     serialFd = serial.Serial(serialName, 115200, timeout=60)
#
#     print("check which port was really used >", serialFd.name)

import serial.tools.list_ports

port_list = list(serial.tools.list_ports.comports())
while len(port_list) == 0:
    port_list = list(serial.tools.list_ports.comports())
comlist = []
for i in range(0, len(port_list)):
    comlist.append(port_list[i][0])
print(comlist)
