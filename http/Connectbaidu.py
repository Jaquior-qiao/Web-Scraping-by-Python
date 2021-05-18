"""
    # There are some work need to accomplish
    # print the HEAD and save the web content into html
    # this way is just print in console

"""
from socket import *
str = b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n'
s = socket(AF_INET, SOCK_STREAM)
s.connect(("www.baidu.com", 80))
s.send(str)
data = s.recv(1024)
num = 0
while data:
    # according to the content-size to break while
    if num - 1 > 14615 / 1024:
        break
    print(data.decode('utf-8'))
    num += 1
    data = s.recv(1024)

s.close()

