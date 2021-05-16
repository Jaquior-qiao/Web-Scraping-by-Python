from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(("127.0.0.1", 6666))
print("Set UDP on 6666")

while True:
    data, addr = s.recvfrom(1024)
    print("Received from %s:%s" % addr, data.decode('utf-8'))
    s.sendto(b'welcome! %s!' % data, addr)
