#!/usr/bin/env python3
# coding=utf-8

import os
print(os.name)
print(os.environ)
print(os.environ.get('PATH'))
print('=========================================')
# 当前目录
print(os.path.abspath('.'))
print(os.pardir)
# 要创建的目录的路径
p = os.path.join(os.path.abspath('.'),'new_dir')
# 创建目录
os.mkdir(p)
# 删除目录
os.rmdir(p)

dir_name = os.path.split('C:/Users/imnot/Code/Python/py_basic/files/test.txt')
print(dir_name[1])
file_name = dir_name[1]
names = file_name.split('.')
print('.'+ names[-1])
dir_name1 = os.path.splitext('C:/Users/imnot/Code/Python/py_basic/files/test.txt')
print(dir_name1[1])