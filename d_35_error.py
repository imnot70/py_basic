#!/usr/bin/env python3
# coding=utf-8

import logging

try:
    print('try')
    result = 10/0
    print('result:%s' % result)
except ZeroDivisionError as e:
    print('error:',e)
finally:
    print('finally')

# 所有的异常都是继承自BaseException，捕获异常时，应先写子类异常
# 类继承关系 https://docs.python.org/3/library/exceptions.html#exception-hierarchy

try:
    print('try')
    r1 = 10 / int('2')
    print('r1:%s' % r1)
except ValueError as ve:
    print('error:',ve)
except ZeroDivisionError as zde:
    print('error:',zde)
# else和expect配合使用，如果没有异常，可以直接进入else
else:
    print('no error')
finally:
    print('finally')

print('===============================')

# 打印信息
try:
    r2=10/0
except ZeroDivisionError as e:
    
    logging.exception(e)
finally:
    print('finally')

print('===============================')

def foo(val):
    n = int(val)
    if n == 0:
        raise ValueError('invalid value:' , n)
    return 10 / 0

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('error value')
        raise

bar()