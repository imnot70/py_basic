#!/usr/bin/env python3
# coding=utf-8

# 以student类为例，(object)表示从哪个类继承下来
class Student(object):
    # 由于类可以起到模板的作用，因此，可以在创建实例的时候，
    # 把一些我们认为必须绑定的属性强制填写进去。、
    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把 name，score 等属性绑上去
    # __init__方法的第一个参数永远是 self，表示创建的实例本身
    # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
    # 但 self 不需要传，Python 解释器自己会把实例变量传进去
    def __init__(self,name,score):
        # Student对象拥有name和score属性
        self.name = name
        self.score = score
    
    # 类中定义的函数第一个参数永远是实例变量self，并且，调用时不用传递该参数
    def print_score(self):
        print('%s: %s' % (self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

s_a = Student('a',97)
s_b = Student('b',96)

s_a.print_score()
s_b.print_score()

s_c = Student('d',94)
# 更改对象的属性值
s_c.name = 'c'
s_c.score = 95
s_c.print_score()

print(s_c.get_grade())