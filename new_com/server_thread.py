import socket

s = socket.socket()
s.bind(('',6667))

while True:
    s.listen(5)
    c, addr = s.accept()
    c.send('Thank You')
    msg_recebida = str(c.recv(1024))
    print msg_recebida
    c.close()
    if msg_recebida == '#':
        print "fechando!"
        s.close()
        break
    
