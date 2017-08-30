#coding: utf-8

import json

"""
@file: test.py
@time: 2017/8/30 
@author: chenfan
"""

a = "just test"
json.dump(a,open('test.json','w'))

b = json.load(open('test.json','r'))
print b