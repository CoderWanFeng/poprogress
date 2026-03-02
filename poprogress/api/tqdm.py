# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@读者群     ：https://www.python4office.cn/wechat-group/
@个人网站 ：www.python-office.com
@Date    ：2023/3/21 22:37 
@Description     ：
'''
from tqdm import tqdm


def simple_progress(base, desc=None, log=True):
    if log and desc:
        return tqdm(iterable=base, desc=desc)
    elif log:
        return tqdm(iterable=base)
    else:
        return base
