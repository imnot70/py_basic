#!/usr/bin/env python3
# coding=utf-8

from io import StringIO,BytesIO

s_w = StringIO()
# 返回本次写入的长度
print(s_w.write('hello'))
print(s_w.write(' '))
print(s_w.write('world'))
# getValue获取写入后的值
print(s_w.getvalue())

b_w = BytesIO()
b_w.write('中文'.encode('utf-8'))
print(b_w.getvalue())