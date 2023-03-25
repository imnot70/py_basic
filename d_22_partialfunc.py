#!/usr/bin/env python3
# coding=utf8
import functools
# 通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点
# 以int函数为例
# 一般调用，可以将字符串转换为int，默认地认为字符是10进制
print(int('12345'))
# 可以通过设置base属性，按其他进制转换
# 8进制的12345转为10进制
print(int('12345',base=8))
# 16进制12345E转为10进制
print(int('12345E',16))
print(int('1001010',2))

# 为方便调用，可以进行封装，如：
def int2(x,base=2):
    return int(x,base)
# 调用（base使用默认值2）
print(int2('1010101'))
# 也可以使用偏函数简化调用
int2p=functools.partial(int,base=2)
print(int2p('1010101'))
int16=functools.partial(int,base=16)
print(int16('12345E'))
