#!/usr/bin/env python3
# coding=utf-8

# 访问限制，把name,score增加__前缀，就变成了私有变量
# 这种变量无法直接访问，需要增加set/get方法
# 需要注意的是，在Python中，变量名类似__xxx__的，
# 也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，
# 不是private变量，所以，不能用__name__、__score__这样的变量名
# _前缀的变量不是私有变量，但是按约定，还是尽量按私有变量的方式处理

# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量

class TestStudent(object):
    
    def __init__(self,name,score):
        self.__name = name
        self.__score =score

    def print_socre(self):
        print('%s: %s' % (self.__name,self.__score))
    
    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name
    
    def get_score(self):
        return self.__score

    def set_score(self,score):
        if(0<= score <=100):
            self.__score =score
        else:
            raise ValueError('bad score')

a=TestStudent('a',99)
a.set_name('b')
print(a.get_name())
a.print_socre()