#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

# map()函数接收两个参数，一个是函数，一个是 Iterable，
# map 将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator 返回
# 比如我们有一个函数 f(x)=x2，要把这个函数作用在一个 list [1, 2, 3, 4, 5, 6, 7, 8, 9]上
# 可以用 map()实现如下
def f(x):
    return x * x

r = map(f,range(1,10))
# 注意返回结果r是Iterator，Iterator是惰性序列，因此需要使用list函数
print(list(r))

# 生成式
l = [x * x for x in range(1,10)]
print(l)

# 把数字转为字符
r_str = map(str,range(1,10))
print(list(r_str))

# reduce 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce 把结果继续和序列的下一个元素做累积计算
# 比如把1，3，5，7，9转换为13579
def fn(x,y):
    return x * 10 + y
i = reduce(fn,[1,3,5,7,9])
print(i)