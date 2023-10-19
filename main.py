# 2023-10-20

# import serial
import time

import serial.tools.list_ports

serPort = 1

ports = serial.tools.list_ports.comports()

for port in ports:
    print(port.device)

port = ports[serPort].device
print(ports[serPort].device)
baud = 9600
ser = serial.Serial(port, baudrate=baud)

try:
    print("Serial connection established !")

    while True:
        line = ser.readline().decode().strip()
        if line:
            # print(line)
            print("%1d-%1d-%02d_%02d.%02d-%02d" % time.localtime()[0:6], sep='', end='')
            print(" _ ", line)

            # print(res, '\t')
            # print(res.tm_year, res.tm_mon, '-', res.tm_mday, '_',
            #       res.tm_hour, res.tm_min)

except serial.SerialException as se:
    print("Serial port error: ", str(se))

except KeyboardInterrupt:
    pass

finally:
    if ser.is_open:
        ser.close()
        print("Serial connection closed.")

# def say_hello():
#     print('hello')
#
#
# def add_label():
#     label = tk.Label(win, text='new')
#     label.pack()


# import tkinter as tk
#
# win = tk.Tk()
# photo = tk.PhotoImage(file='100.png')
# win.iconphoto(False, photo)
# win.config(bg='#C0C0C0')
# win.title("Zasor2")
# win.geometry("500x600+100+200")
# win.resizable(True, True)
#
# label_1 = tk.Label(win, text='Взвесить',
#                    bg='#A52A2A',
#                    fg='white',
#                    font=('Arial', 25, 'bold'),
#                    # padx=50,
#                    # pady=100,
#                    width=10,
#                    height=3,
#                    # anchor='sw',
#                    relief=tk.RAISED,
#                    bd=10,
#                    justify=tk.CENTER)
#
# btn_1 = tk.Button(win, text='Взвесить',
#                   command=say_hello)
#
# btn_2 = tk.Button(win, text='Готово',
#                   command=add_label,
#                   activebackground='blue',
#                   bg='red',
#                   state=tk.NORMAL)
#
# label_1.pack()
# btn_1.pack()
# btn_2.pack()
#
# line = ser.readline().decode().strip()
# if line:
#     print(line)
#
# win.mainloop()
#
#
#
# try:
#     print("Serial connection established !")
#
#     while True:
#         line = ser.readline().decode().strip()
#         if line:
#             print(line)
#             # print("%02d%02d-%02d_%02d%02d%02d" % time.localtime()[0:6], " _ ", line)
#
#             # print(res, '\t')
#             # print(res.tm_year, res.tm_mon, '-', res.tm_mday, '_',
#             #       res.tm_hour, res.tm_min)
#
#
#
#
#
# except serial.SerialException as se:
#     print("Serial port error: ", str(se))
#
# except KeyboardInterrupt:
#     pass
#
# finally:
#     if ser.is_open:
#         ser.close()
#         print("Serial connection closed.")
