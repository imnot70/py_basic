#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools

# 准备工作，定义一个函数
def now():
    print("2023-03-25")

f = now
f()

# 函数对象有一个__name__属性，可以拿到函数的名字
func_name = now.__name__
print(func_name)
print(f.__name__)

print('=============================')

# 对now函数进行增强，在前打印日志
# log函数就是一个装饰器
def log(func):
    def wrapper(*args,**kw):
        print('call func%s():' % func.__name__)
        return func(*args,**kw)
    return wrapper
# 使用@语法，把装饰器置于函数为的定义处
@log
def now1():
    print('2023-03-25')
# 调用now1，会先执行装饰器，相当于执行了语句
# now1 = log(now1)
now1()
# 这是now1指向的已经是wrapper了
print(now1.__name__)
# 需要把装饰器中的wrapper改为now1，否则有些依赖函数名的代码会报错
# 但是并不需要编写wrapper.__name__ = func.__name__这样的代码
# 可以利用functools.wraps函数
def log1(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call func:%s()' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log1
def now2():
    print('2023-03-25')

print('=============================')
now2()
print(now2.__name__)
