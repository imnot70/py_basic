#!/usr/bin/env python3
# coding=utf-8

import subprocess,os,time,random
from multiprocessing import Process,Queue

# 子进程
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

r = subprocess.call(['nslookup','www.baidu.com'])
print('Exit code:',r)

print('===============================')

# 进程间通信，创建两个子进程，一个往Queue中写入数据，一个从Queue中读取数据

def write(q):
    print('Process to write: %s' % os.getpid())
    for v in ['A','B','C']:
        print('Put %s to queue...' % v)
        q.put(v)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        v = q.get(True)
        print('Get %s from queue.' % v)

if __name__ == '__main__':
    # 创建一个队列，给子进程读写使用
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=write,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    # 死循环，只能终止
    pr.terminate()
