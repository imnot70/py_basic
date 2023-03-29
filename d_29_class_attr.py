#!/usr/bin/env python3
# coding=utf-8

# 由于Python是动态语言，根据类创建的实例可以任意绑定属性
# 可以直接在 class 中定义属性，这种属性是类属性，归类所有
class ClassAttr(object):
    # 类的name属性
    name = 'ClassAttr'

    # 实例对象的name属性
    def set_name(self,name):
       self.name = name

ca = ClassAttr()
# 类的name
print(ClassAttr.name)
ca.set_name('test')
# 实例对象ca的name
print(ca.name)