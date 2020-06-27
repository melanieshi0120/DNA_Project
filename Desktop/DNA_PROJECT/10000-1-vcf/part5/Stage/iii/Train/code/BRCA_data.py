# coding:utf-8

import numpy as np

#读取规定格式的文件
# 例：1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0	0，1
#患病     0，1
#不患病    1，0
def readCase(path):
    F = open(path, 'r')

    L = []

    for line in F:
        lst = line.strip()
        L.append(lst)

    return L