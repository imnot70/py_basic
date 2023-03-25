#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 内置函数 https://docs.python.org/3/library/functions.html
def abs_test(x):
    if not isinstance(x,(float,int)):
        raise TypeError("类型不正确")
    if x >= 0:
        return x
    else:
        return -x
def multi_return_value():
    return 10,100