#!/usr/bin/env python3
# coding=utf-8

# 配合test_d_37_unittest.py使用
# 实现功能，通过对象的属性访问值，如：
# d = Dict(a=1)
# d.a
# 输出：1
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
    
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self,key,value):
        self[key] = value

