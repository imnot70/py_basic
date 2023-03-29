#!/usr/bin/env python3
# coding=utf-8

import functools

# python内置的的@property装饰器可以把一个方法变成属性调用
class ClassProp(object):

    # 把获取score的函数变成一个属性，即在类中添加了score属性
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')
        elif value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value

cp = ClassProp()
cp.score=60
print(cp.score)
cp.score=999