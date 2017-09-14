#!/usr/bin/python
# -*- coding: utf-8 -*-
from threading import Thread
import socket
import datetime
from Tkinter import *
import sys

class ServerTh(Thread):

    def __init__(self, tk_ui, host, port):
        Thread.__init__(self)
        self.s = socket.socket()
        self.host = host
        self.port = int(port)
        self.file_bd = open('conversas.txt','w')
        self.ui = tk_ui
        self.running = True
        self.s.bind((self.host, self.port))

    def run(self):
        try:
            while self.ui.running == True:
                self.s.settimeout(5)
                self.s.listen(5)
                print "Server Iniciado"
                c, addr = self.s.accept()
                print 'Got connection from', addr
                c.send('Thank you for connecting')
                msg_recebida = str(c.recv(1024))
                print msg_recebida
                msg_final = msg_recebida.split(';')
                print msg_final
                msg_temp = '%s:    %s' % (msg_final[0], msg_final[1])
                self.ui.e3.insert(END, str(msg_temp + '\n'))
                self.ui.e3.see(END)
                new_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
                msg_to_write = '%s;%s;%s' % (msg_final[0], msg_final[1], new_date)
                self.file_bd.write(msg_to_write)
                c.send('mensagem recebida: ' + msg_final[1])
                c.close()

        except:
            pass
        

class GUI_TK(Thread):
    def __init__(self, host, port, ext_host, ext_port):
        Thread.__init__(self)
        self.port = int(ext_port)
        self.host = ext_host
        self.running = True
        self.server = ServerTh(self, host, port)



    def send_message(self):
        s = socket.socket()
        host = self.host
        port = self.port
        s.connect((self.host,self.port))
        print host
        print s.recv(1024)
        s.send(self.e1.get() + ';' + self.e2.get())
        msg_sent = '%s:    %s' % (str(self.e1.get()), str(self.e2.get()))
        self.e3.insert(END,str(msg_sent + '\n'))
        self.e2.delete(0,'end')
        self.file_bd = open('conversas.txt', 'w')
        self.file_bd.write(msg_sent)
        self.file_bd.close()
        s.close()

    def callback(self):
        print "Quiting"
        self.running = False
        self.server.running = False
        self.master.destroy()
        self.master.quit()
        raise SystemExit

    def run(self):
        self.master = Tk()
        self.new_text = StringVar()
        self.master.protocol("WM_DELETE_WINDOW", self.callback)
        self.label1 = Label(self.master, text="User").grid(row=0)
        self.label2 = Label(self.master, text="Message").grid(row=1)
        self.e1 = Entry(self.master)
        self.e2 = Entry(self.master)
        self.e3 = Text(self.master, height=4)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.b1 = Button(self.master, text='Quit', command=self.callback).grid(row=3, column=0, sticky=W, pady=4)
        self.b2 = Button(self.master, text='Send', command=self.send_message).grid(row=3, column=1, sticky=W, pady=4)
        self.server.start()
        self.master.mainloop()


if __name__ == "__main__":
    print u'_____________________ Faça o Login ________________________'
    user = raw_input('Digite o seu IP: ')
    sua_porta = raw_input('Digite sua Porta: ')
    external = raw_input('Digite o IP do receptor: ')
    ext_port = raw_input('Digita a porta do receptor: ')

    client = GUI_TK(user, sua_porta, external, ext_port)
    client.start()

    sys.exit()

