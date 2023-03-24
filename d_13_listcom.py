#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

l1 = list(range(1, 11))
print(l1)

# 生成[1x1, 2x2, 3x3, ..., 10x10]
# 方式1
l2 = []
for n in range(1, 11):
    l2.append(n*n)
print(l2)

# 方式2
l3 = [n * n for n in range(1, 11)]
print(l3)
# 方式2附加条件(n*n为偶数)
l4 = [n*n for n in range(1, 11) if n*n % 2 == 0]
print(l4)

# 生成全排列
l5 = [m+n for m in 'abc' for n in 'xyz']
print(l5)

l6 = [d for d in os.listdir('.')]
print(l6)
