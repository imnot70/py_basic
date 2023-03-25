#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数
l=list(map(lambda x: x * x,range(1,10)))
print(l)