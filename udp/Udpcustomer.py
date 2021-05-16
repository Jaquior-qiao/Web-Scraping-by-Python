from socket import *

s = socket(AF_INET, SOCK_DGRAM)
for data in [b'Tom', b'Jerry', b"Spike"]:
    s.sendto(data, ('127.0.0.1', 6666))
    print(s.recv(1024).decode('utf-8'))
s.close()
