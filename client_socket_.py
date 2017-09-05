#!/usr/bin/python

import socket
import os
from Tkinter import *
import threading

r = socket.socket()
host = socket.gethostname()
port = 6669
r.bind((host, port))
r.listen(5)

def send_message():
    s = socket.socket()
    host = socket.gethostname()
    port = 6667
    s.connect((host, port))
    print host
    print s.recv(1024)
    s.send(e1.get() + ';' + e2.get())
    s.close()

def listen_message():
    while True:
        c, addr = r.accept()
        print 'Got connection from', addr
        msg_recebida = str(c.recv(1024))
        print msg_recebida

master = Tk()
Label(master, text="User").grid(row=0)
Label(master, text="Message").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Send', command=send_message).grid(row=3, column=1, sticky=W, pady=4)



mainloop( )

r.close()

# os.system('clear')
# print 'Conectado ao MESSENGER!\n'
# user = raw_input('Seu Nome de Usuario: ')

# while True:
#     s = socket.socket()
#     host = socket.gethostname()
#     port = 6667
#
#     msg = raw_input(':')
#     if msg == 'quit()':
#         s.close()
#         break
#     s.connect((host, port))
#     print s.recv(1024)
#     s.send(user + ';' + msg + '\n')
#     s.close()



