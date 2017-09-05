#!/usr/bin/python
from threading import Thread
import socket
import datetime
from Tkinter import *
import sys

class ServerTh(Thread):

    def __init__(self, tk_ui, host, port):
        Thread.__init__(self)
        self.s = socket.socket()
        self.host = str(host)
        self.port = 6669
        self.s.bind((self.host, self.port))
        self.file_bd = open('conversas.txt','a')
        self.ui = tk_ui


    def run(self):
        self.s.listen(5)

        print "Server Iniciado"
        while True:
            c, addr = self.s.accept()
            print 'Got connection from', addr
            c.send('Thank you for connecting')
            msg_recebida = str(c.recv(1024))
            print msg_recebida
            msg_final = msg_recebida.split(';')
            print msg_final
            self.ui.e3.insert(END,str(msg_final[1]) + '\n')
            self.ui.e3.see(END)
            new_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
            msg_to_write = '%s;%s;%s' % (msg_final[0],msg_final[1],new_date)
            self.file_bd.write(msg_to_write)
            c.send('mensagem recebida: ' + msg_final[1])
        c.close()
	sys.exit()


class GUI_TK(Thread):
    def __init__(self,myport,other_host):
        Thread.__init__(self)
        self.port = myport
	self.host = str(other_host)


    def send_message(self):
        s = socket.socket()
        host = self.host
        port = self.port
        s.connect((host, port))
        print host
        print s.recv(1024)
        s.send(self.e1.get() + ';' + self.e2.get())
        s.close()

    def callback(self):
        self.master.quit()
	sys.exit()
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
        self.master.mainloop()


if __name__ == "__main__":
    client = GUI_TK(int(sys.argv[3]), sys.argv[4])
    client.start()
    server = ServerTh(client, sys.argv[1], int(sys.argv[2]))
    server.start()
    sys.exit()

