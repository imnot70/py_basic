#!/usr/bin/env python3
# coding=utf-8

# 多重继承

# 所有类的基类
class Animal(object):
    pass

# 哺乳动物类
class Mammal(Animal):
    pass

# 鸟类
class Bird(Animal):
    pass

# 可奔跑的
class Runnable(object):
    def run(self):
        self.run()

# 可飞行的
class Flyable(object):
    def fly(self):
        self.fly()

# 犬类，继承自哺乳动物，同时可以继承自Runnable
class Dog(Mammal,Runnable):
    pass

# 蝙蝠，继承自哺乳动物，同时可继承自Flyable
class Bat(Mammal,Flyable):
    pass

# 鹦鹉，继承自鸟类
class Parrot(Bird,Flyable):
    pass

# 鸵鸟，继承自鸟类
class Ostrich(Bird,Runnable):
    pass

