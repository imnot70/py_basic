#!/usr/bin/env python3
# coding=utf-8

from d_25_oop import Student
from d_27_inherit import Animal
from d_27_inherit import Dog
import types

# 获取对象信息
# 使用type()
print(type(123))
print(type('123'))
print(type(None))
print(type(abs))
s=Student('a',99)
print(s)

print('===============================')

# 判断一个对象是否是函数
def fn():
    pass

print(type(abs) == types.FunctionType)
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x*x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

print('===============================')

# 使用isinstance()
a = Animal()
d = Dog()

print(isinstance(a,Dog))
print(isinstance(d,Animal))
print(isinstance(d,Dog))
print(issubclass(Dog,Animal))

print('===============================')

# 使用dir(),如果要获得一个对象的所有属性和方法，可以使用 dir()函数
print(dir(a))
print(dir(d))

# hasattr(),判断对象是否有某个属性
print(hasattr(s,'name'))
# setattr(),设置对象的属性值
setattr(s,'name','s')
print(s.name)
# getattr(),获取对象的属性值
print(getattr(s,'name'))