# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 03:53:41 2021

@author: Furcas
"""

class SpesialNum(object):
    def __init__(self, num:int):
        self.num = num
    
    def __add__(self, other):
        sum_nums = self.num+other.num
        return SpesialNum(sum_nums)
    
    