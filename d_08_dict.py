#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 类似于其他语言中的map
# 声明一个dict
d={'a':97,'b':90,'c':85}
# 根据key获取value，如果key不存在会报错
print(d['a'])

# 通过get方法获取value，key不存在可以返回None或者自己指定的值
print(d.get('d'))
print(d.get('e',10))
print(d.get("a"))

# 删除一个key-value
d.pop('a')
print(d.get('a'))