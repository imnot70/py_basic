#!/usr/bin/env python3
# coding=utf-8

import logging
logging.basicConfig(level= logging.INFO)

# 启动Python解释器时可以用-O 参数来关闭assert
# python3 -0 xxxx.py

def foo(s):
    n = int(s)
    # 使用断言，如果断言失败，会拋出AssertionError
    assert n != 0, 's is zero'
    print(10/n)

def main():
    foo('1')

main()

def log_error(s):
    n = int(s)
    logging.info('n = %d' % n)
    print(10/n)

log_error('5')