#!/usr/bin/env python3
# coding=utf-8

# 读取文件

f = open('./files/test.txt','r')
s = f.read()
print(s)
f.close()

# 加上try finally
print('======================')
try:
    # r 文本模式读取，rb 二进制模式读取
    f1=open('./files/test.txt','r')
    print(f1.read())
finally:
    if f1:
        f1.close()

# 使用with代替try finally
print('======================')
with open('./files/test.txt','r') as f2:
    print(f2.read().strip())

'''
print('======================')
with open('./pics/Pixiv_0002.jpg','rb') as img:
    print(img.read())
'''

print('=======================')
# 写文件
with open('./files/test1.txt','w',encoding='utf-8') as file_writer:
    file_writer.write('test content,write by python')