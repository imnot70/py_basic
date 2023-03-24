#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 变量f指向函数abs
f=abs
print(f(-10))

# 函数中传入函数
def test(x,y,f):
    return f(x) + f(y)

print(test(-5,6,abs))

def pow(x):
    return x * x
print(test(5,6,pow))