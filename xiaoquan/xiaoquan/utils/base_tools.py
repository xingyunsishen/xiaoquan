#!/usr/share/app/anaconda3/bin/python3
# -*- coding: utf-8 -*-

""" 
@version: v1.0 
@author: pu_yongjun
"""
import hashlib


def gen_md5(str_con):
    """ 把输入的数据转换成MD5
    :param str_con: 输入的数据
    :return:
    """
    hl = hashlib.md5()
    hl.update(str(str_con).encode(encoding='utf-8'))
    return hl.hexdigest()
