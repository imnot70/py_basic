#!/usr/bin/env python3
# coding=utf-8

from enum import Enum,unique

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():
    # value 属性则是自动赋给成员的 int 常量，默认从 1 开始计数
    print(name,'=>',member,',',member.value)

# 如果要更精确的控制枚举，可以从Enum派生出自定义类
# @unique装饰器可以检查值是否有重复
@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

for name,member in Weekday.__members__.items():
    print(name,'=>',member,',',member.value)