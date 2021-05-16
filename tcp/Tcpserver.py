"""
    based on ipv4 & tcp
    the question I find:
        write this like socket(socket.INET,...) when you used the "socket."
        the program would push a error:
            AttributeError: type object 'socket' has no attribute 'AF_INET'
        so just use AF_INET (delete the head of class's name), then will fine.
"""
from socket import *
import threading
import time

# build tcp connection
s = socket(AF_INET, SOCK_STREAM)

# bind the ip and port
s.bind(("127.0.0.1", 6666))

# listen the request of the port
s.listen(5)
print("wait for connection....")


# creat a reflection func
def tcp(sock, addr):
    print("Accept a new connection from%s to %s..." % addr)
    sock.send(b"success!")
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(("welcome %s" % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print("Connection from %s:%s closed." % addr)


while True:
    # accept request of customer
    sock, addr = s.accept()
    # creat new thread to deal tcp
    t = threading.Thread(target=tcp, args=(sock, addr))
    t.start()
