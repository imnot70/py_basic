#!/usr/bin/env python3
# coding=utf8
import sys

# 在Python中，一个.py文件就称之为一个模块（Module）
# 使用模块最大的好处是大大提高了代码的可维护性。
# 其次，编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。
# 我们在编写程序的时候，也经常引用其他模块，包括 Python 内置的模块和来自第三方的模块
# 使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中，
# 因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。
# 但是也要注意，尽量不要与内置函数名字冲突。

# 为了避免模块名冲突，Python 又引入了按目录来组织模块的方法，称为包（Package）。
# 现在，假设我们的 abc 和 xyz 这两个模块名字与其他模块冲突了，
# 于是我们可以通过包来组织模块，避免冲突。
# 方法是选择一个顶层包名，比如 mycompany，按照如下目录存放
# |- mycompany
#  |- __init__.py
#  |- abc.py
#  |- xyz.py
# 引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。
# 现在，abc.py 模块的名字就变成了 mycompany.abc，类似的，xyz.py的模块名变成了 mycompany.xyz
# 注意，每一个包目录下面都会有一个__init__.py 的文件，
# 这个文件是必须存在的，否则，Python 就把这个目录当成普通目录，而不是一个包。
# __init__.py 可以是空文件，也可以有 Python 代码，
# 因为__init__.py 本身就是一个模块，而它的模块名就是 mycompany。
# 类似的，可以有多级目录，组成多级层次的包结构，比如
# |- mycompany
#    |- web
#    |- __init__.py
#    |- utils.py
#    |- abc.py
#  |- __init__.py
#  |- abc.py
#  |- xyz.py
# 自己创建模块时要注意命名，不能和 Python 自带的模块名称冲突。
# 例如，系统自带了 sys 模块，自己的模块就不可命名为 sys.py，
# 否则将无法导入系统自带的 sys 模块

# 任何模块代码的第一个字符串都被视为模块的文档注释
'a test module'
# 模块作者
__author__='zp'

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args) ==2:
        print('hello,%s' % args[1])
    else:
        print('too many arguments')

if __name__ == '__main__':
    test()
