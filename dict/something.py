#coding: utf-8

"""
@file: something.py
@time: 2017/8/29 
@author: chenfan
"""
###字典常用操作

d = {
    "name":"tom",
    "age":18,
    "school":"swu",
    "nova":""
}
#bad
if d.has_key('name'):#python3移除
    print d['name']
#google
if 'name' in d:
    print d['name']

#获取,key不存在
print(d.get('name','default'))
print(d.get('other','default'))

nd = {}
for k,v in d.items():
    nd[k] = v
print nd


