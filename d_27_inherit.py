#!/usr/bin/env python3
# coding=utf-8

# 当我们编写一个class的时候，我们可以从现有的class继承
# 比如现在有一个类Animal，类中有一个方法run，可以直接打印
class Animal(object):
    def run(self):
        print('Animal is running')

# 当需要Cat和Dog类时，如果继承自Animal，就不需要再编写run
class Cat(Animal):
    pass

class Dog(Animal):
    # 重写
    def run(self):
        print('Dog is running')
    
    def eat(self):
        print('Dog is eatting')

# Cat可以直接调用run方法
c = Cat()
c.run()

d = Dog()
d.eat()
d.run()

# 这是传入的对象不一定是Animal或者它的子类，但是只要保证有一个run函数就可以执行
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())