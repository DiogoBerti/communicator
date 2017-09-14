import socket


s = socket.socket()
s.connect(('192.168.16.63',6667))
s.send('#')
s.close()


