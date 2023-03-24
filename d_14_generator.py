#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 当一个函数包含yield之后，就不再是一个普通的函数，而是一个生成器
# 函数和生成器的区别
# 函数是顺序执行，遇到 return 语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到 yield 语句返回，
# 再次执行时从上次返回的 yield 语句处继续执行

g1 = (x * x for x in range(10))
print(g1)
for n in g1:
    print(n)

# 手写的斐波那契函数


def fib_func(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib_func(10)

# 生成器方式，一个函数包含yield就不再是函数，而是一个生成器


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    return 'done'

print('=======================')
f = fib(10)
for n in f:
    print(n)

print('=======================')
f1=fib(10)
while True:
    try:
        print(next(f1))
    except StopIteration as e:
        print(e.value)
        break
