#!/usr/bin/env python3
# coding=utf-8

import threading,time

# 多线程
def loop():
    print('Thead:[%s] is running' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# Lock，多线程中，变量由线程间共享。需要使用Lock对资源进行锁定
# 锁可以通过threading.lock()创建

balance =0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

def change_it(n):
    global balance
    balance = balance + n
    # print(balance)
    balance = balance - n
    # print(balance)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)