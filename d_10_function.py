#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from f_01_abs import abs_test
from f_01_abs import multi_return_value
# 内置函数
print(abs(-100))
print(max(1, 2, 3))
print(int('123'))
print(str(123))
print(bool(1))
print(bool(0))

# 定义函数
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x

# pass可以什么都不做，只占位
def my_pass():
    pass

# 参数默认值，n=2
def power(x, n=2):
    total = 1
    while n > 0:
        total *= x
        n -= 1
    return total

print(my_abs(-10))
print(abs_test(-100))

print(multi_return_value())
print(power(5,3))

# 多个参数，调用时，参数顺序与参数列表不同时，需要指明参数名
def register(name,gender,age=10,city='tj'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

register('a','f',7)
# 第三个参数是city，需要指明参数名
register('b','m',city='bj')

# 可变参数
def calc(*numbers):
    sum=0
    for n in numbers:
        sum += n
    return sum

print(calc(1,2,3))
l=[1,2,3,4]
# 直接使用数组
print(calc(*l))

# 关键字参数
def person(name,age,**kw):
    # 处理kw中的字段
    if 'job' in kw:
        pass
    print('name:',name,',age:',age,',other:',kw)

# 调用
person('a',18)
# 后面的参数会自动封装为dict
person('b',19,city='bj')
person('c',20,salary=100.0,city='tj')
extra={'job':'engineer','salary': 500.0}
person('d',21,**extra)

# 只接收job和city参数，使用*分隔，*后面的参数被视为命名关键字参数，关键字参数调用时如果不写明参数名会报错
def person_limit(name,age,*,job,city='bj'):
    print('name:',name,',age:',age,',job:',job,',city:',city)

person_limit('a',24,job='engineer',city='bj')

# 多种参数混合使用时，顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2)
f1(1,2,3)
l1=['l1','l2']
f1(1,2,3,*l1,kw1='kw1',kw2='kw2')
f1(1,2,3,*('a','b'),**{'kw1':'kw1','kw2':'kw2'})
f1('test',10,1,'arg1','arg2',kw1='kw1')
f2('test',10,d='a',kw1='kw1',kw2='kw2')

# 递归
def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)
print(fact(4))
print(fact(5))