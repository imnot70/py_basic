#!/usr/bin/env python3
# coding=utf-8
# 用于给实例绑定函数
from types import MethodType

class SlotClass(object):
    pass

sc = SlotClass()
sc.name = 'sc'
print(sc.name)

def set_age(self,age):
    self.age = age

# 绑定
sc.set_age = MethodType(set_age,sc)
# 调用实例对象的set_age
sc.set_age(35)
print(sc.age)

# 但是前面的MethodType的绑定方式，对另一个实例是无效的
# sc1 = SlotClass()
# print(sc1.age)
# 因此可以给类对象绑定函数
def set_score(self,score):
    self.score =score
SlotClass.set_score = MethodType(set_score,SlotClass)
sc1 = SlotClass()
# 所有的实例都可以使用set_score
sc1.set_score(100)
print(sc1.score)

# 使用__slots__限制实例可以绑定的属性
# 注意，__slots__限制的属性只对当前的类有效，对子类无效
class SlotClass1(object):
    # 限制属性
    __slots__=('name','age')

sc2 = SlotClass1()
sc2.name = 'sc2'
sc2.age = 19
# 无法为实例绑定score属性
# sc2.score = 100
