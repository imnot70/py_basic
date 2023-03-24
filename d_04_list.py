#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# list 是一种有序的集合，可以随时添加和删除其中的元素
classmate = ['a', 'b', 'c']
print(classmate)
len(classmate)
print(classmate[0])
print(classmate[1])
print(classmate[2])
print(classmate[-1])
print(classmate[-2])
print(classmate[-3])

# 追加
classmate.append('d')
print(classmate)

# 插入
classmate.insert(2, 'e')
print(classmate)

# 弹出最后的元素
ele = classmate.pop()
print(ele)
# 弹出指定位置的元素
ele = classmate.pop(2)
print(ele)
# 对某一位上直接赋值，但是超过当前数组长度会报错
classmate[0] = 'f'
print(classmate)
# 数组中可以是不同的类型
l1=[123,'a',True,[1,2,3]]
print(l1)
print(len(l1))

# 使用list和range生成数组
l2 = list(range(10))
for e in l2:
    print(e)