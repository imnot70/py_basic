#!/usr/bin/env python3
# coding=utf8

from PIL import Image
import sys

# 在python中安装第三方模块是通过pip完成的
# 以安装基于Python Imaging Library的Pillow为例
# 一般来说，第三方库都会在 Python 官方的 pypi.python.org 网站注册，
# 要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，
# 比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：
# pip install Pillow
img = Image.open('./pics/Pixiv_0002.jpg')
print(img.format,img.size,img.mode)
# img.thumbnail((200,100))
# img.save('thumbnail.jpg','JPEG')

# 其他常用的第三方库还有:
# mysql驱动：mysql-connector-python
# 科学计算：numpy
# 生成文本的模板工具：Jinja2

# 当我们试图加载一个模块时，Python 会在指定的路径下搜索对应的.py文件，如果找不到，就会报错
# 默认情况下，Python 解释器会搜索当前目录、所有已安装的内置模块和第三方模块，
# 搜索路径存放在 sys 模块的 path 变量
print(sys.path)

# 如果我们要添加自己的搜索目录，有两种方法
# 一是直接修改 sys.path，添加要搜索的目录：sys.path.append('需要添加的路径')
# 这种方法是在运行时修改，运行结束后失效
# 第二种方法是设置环境变量 PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
# 设置方式与设置 Path 环境变量类似。注意只需要添加你自己的搜索路径，Python 自己本身的搜索路径不受影响
