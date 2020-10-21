# coding=UTF-8

"""import serial.tools.list_ports

plist = list(serial.tools.list_ports.comports())

if len(plist) <= 0:
    print ("The Serial port can't find!")
else:
    plist_0 =list(plist[0])
    serialName = plist_0[0]
    serialFd = serial.Serial(serialName,115200,timeout = 10)
    print ("check which port was really used >",serialFd.name)
print(serialFd.isOpen())
serialFd.write()

serialFd.write('reboot'.encode())
i=1
for i in range(1,100):
    print(serialFd.readline())
"""

impo

def poweroffSchedule():
    ser = serial.Serial("COM5", 115200, timeout=0.5)
    ser.write('root'.encode())
    print(ser.readline());


if __name__ == "__main__":

    poweroffSchedule()