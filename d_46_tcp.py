#!/usr/bin/env python3
# coding=utf-8

import socket

def use_tcp():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        # s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('www.sina.com.cn',80))
        s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
        buffer = []
        while True:
            # 每次最多接收 1k 字节:
            d = s.recv(1024)
            if d:
                buffer.append(d)
            else:
                break
        data = b''.join(buffer)
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    with open('sina.html','wb') as f:
        f.write(html)
    
if __name__ == '__main__':
    use_tcp()
    print('==========================')
