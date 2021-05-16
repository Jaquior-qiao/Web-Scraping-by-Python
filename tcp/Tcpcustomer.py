from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 6666))
print(s.recv(1024).decode('utf-8'))

for data in [b'Tom', b'Jerry', b"Spike"]:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b"exit")
s.close()


