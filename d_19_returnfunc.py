#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 一般的求和函数
def calc_sum(*args):
    result = 0
    for n in args:
        result += n
    return result
print(calc_sum(*range(101)))

# 不需要立刻求和，而是在后面的代码中，根据需要再计算
def lazy_sum(*args):
    def sum():
        result=0
        for n in args:
            result += n
        return result
    return sum
# 此时只是返回了sum函数
f=lazy_sum(*range(101))
# 调用f函数时，才是真正的计算过程
print(f())