#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections.abc import Iterable
from collections.abc import Iterator

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key,d[key])

for value in d.values():
    print(value)

for k,v in d.items():
    print(k,v)

for i,key in enumerate(d):
    print(i,key,d[key])

print('d.items is iterable:',isinstance(d.items(),Iterable))

str= "abcdef"
print(isinstance(str,Iterable))
for s in str:
    print(s)

# 生成器都是 Iterator 对象，但 list、dict、str 虽然是 Iterable，却不是Iterator。
# Iterator 对象可以被 next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration 错误，
# Iterator 的计算是惰性的，只有在需要返回下一个数据时它才会计算
# 把 list、dict、str 等 Iterable 变成 Iterator 可以使用 iter()函数
print(isinstance(str,Iterable))
print(isinstance(str,Iterator))
print(isinstance(iter(str),Iterator))
