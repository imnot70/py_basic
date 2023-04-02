#!/usr/bin/env python3
# coding=utf-8

import unittest
from d_37_unittest_dict import Dict

# 编写单元测试时，需要编写一个测试类，从 unittest.TestCase 继承
# 测试的python脚本文件也要以test开头（vscode环境）
class TestDict(unittest.TestCase):
    # 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
    def test_init(self):
        d = Dict(a=1,b='test')
        # 单元测试断言
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertIsInstance(d.b,str)
        self.assertTrue(isinstance(d,Dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key,'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
    def setUp(self):
        print('setUp...')
    
    def setUp(self):
        print('setUp')
    def tearDown(self):
        print('teatDown')
# if '__name__' == '__main__':
#     unittest.main()

'''
运行单元测试的方式
1，在代码最后加入
if __name__ == '__main__':
    unittest.main()
这样，就可以把python单元测试代码当作正常的python脚本运行
2，通过-m unittest参数
python3 -m unittest xxxx.py

setUp 与 tearDown
可以在单元测试中编写两个特殊的 setUp()和 tearDown()方法。这两个方
法会分别在每调用一个测试方法的前后分别被执行
''' 