#!/usr/bin/env python3
# coding=utf-8

import os,time,random
from multiprocessing import Process,Pool

# python的os模块封装了常见的系统调用，其中包括用于创建子进程的fork

# 获取进程号
print('Process (%s) start...' % os.getpid())

# 只在Linux/Unix中可用
'''
pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''

# multiprocessing模块提供了Process类来描述进程

# 子进程要执行的代码
def run(name):
    print('child process,name: %s,pid:%s' % (name,os.getpid()))

if(__name__ == '__main__'):
    print('parent process %s',os.getpid())
    # 创建进程
    p = Process(target=run, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

print('===============================================')

# 使用Pool批量创建进程

def long_time_task(name):
    print('Run task %s(%s)' % (name,os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('The %s run %0.3f sencods' % (name,end-start))

if '__main__' == __name__:
    print('Parent process %s' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    p.close()
    p.join()
    print('done')