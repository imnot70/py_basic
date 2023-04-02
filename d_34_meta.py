#!/usr/bin/env python3
# coding=utf-8

# 以下面的Hello类为例
class Hello(object):
    def hello_world(self):
        print('hello world!')

h=Hello()
h.hello_world()
# 打印结果：<class 'type'>
print(type(Hello))
# 打印结果：<class '__main__.Hello'>
print(type(h))

# type函数打印出的Hello类为type型，h实例的类型为Hello型
# 在python中类的定义是运行时动态创建的，创建类使用的就是type函数
# type函数既可以查看对象的类型，也可以创建出新的类型
# 比如通过type创建Hello类而无需通过 class Hello(object)的形式来定义
# 方式如下

# 先定义函数
def fn(self,name='world'):
    print('Hello %s' % name)

# 创建Hello类，依次定义class名称，父类，函数
Hello1 = type('Hello1',(object,),dict(hello_world=fn))
h1=Hello1()
h1.hello_world()
print('==========================================')

# 除了使用type函数，还可以使用metaclass，使用metaclass的流程是
# 先定义metaclass，再创建class，最后创建实例
# 以定义一个MyList为例，给自定义的MyList增加add方法
# 1，定义ListMetaClass，元类按惯例都是以MetaClass结尾
# 因为metaclass是类的模板，所以需要从type继承下来
class ListMetaClass(type):
    # __new__()函数的参数依次是：当前准备创建的类对象，类名，继承的父类的集合，类的方法的集合
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value : self.append(value)
        return type.__new__(cls,name,bases,attrs)
# 2，有了ListMetaClass，还要在定义类的时候指示使用MetaClass来定制类，传入关键字参数metaclass
# 传入ListMetaClass后，python解释器在创建MyList时，会通过ListMetaClass.__new__()创建，
# 因此，可以在__new__()中对类的定义进行修改，比如加上add方法，再返回修改后的定义
class MyList(list,metaclass=ListMetaClass):
    pass

# 测试add函数（正常的list没有add函数）
l1 = MyList()
l1.add(1)
print(l1)

# 通过metaclass修改类行为的方式，多用于ORM框架中

