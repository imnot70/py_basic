#!/usr/bin/env python3
# coding=utf-8

# 配合d_48_tcp_client使用

import socket,threading,time

def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

def start():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1',18080))
        s.listen(5)
        print('Waiting for connection...')
        while True:
            # 接受一个新连接:
            sock,addr = s.accept()
            # 创建新线程来处理 TCP 连接:
            t = threading.Thread(target=tcplink, args=(sock, addr))
            t.start()

start()