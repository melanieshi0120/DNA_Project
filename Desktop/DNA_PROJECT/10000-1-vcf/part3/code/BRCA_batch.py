# coding:utf-8

import random

#随机选取 batch_size 大小的数据作为batch
def next_batch(L, batch_size):

    Lb = random.sample(L, batch_size)
    Lr = list(set(L) - set(Lb))

    x = []
    y = []

    for l in Lb:
        lst = l.split()
        lst_x = lst[0].split(',')
        lst_y = lst[1].split(',')

        x.append(lst_x)
        y.append(lst_y)

    return x, y, Lr

#选择所有的数据作为返回数据
def all(L):

    x = []
    y = []

    for l in L:
        lst = l.split()
        lst_x = lst[0].split(',')
        lst_y = lst[1].split(',')

        x.append(lst_x)
        y.append(lst_y)

    return x, y

#按照顺序从测试集中挑选一个
def getOne(L):

    Lb = random.sample(L, 1)
    Lr = list(set(L) - set(Lb))

    x = []
    y = []

    for l in Lb:
        lst = l.split()
        lst_x = lst[0].split(',')
        lst_y = lst[1].split(',')

        x.append(lst_x)
        y.append(lst_y)

    return x, y, Lr

#把测试集按照患病和不患病两组分开
def group(L):

    xc = []
    yc = []
    xn = []
    yn = []

    for l in L:
        lst = l.split()
        lst_x = lst[0].split(',')
        lst_y = lst[1].split(',')

        if(lst[1] == '0,1'):
            xc.append(lst_x)
            yc.append(lst_y)
        else:
            xn.append(lst_x)
            yn.append(lst_y)

    print (len(xc),len(xn))
    return xc, yc, xn, yn