#!/usr/bin/env python
# _*_coding:utf8_*_
# __auth:ChenFan

'''
以字典的形式返回数据
'''

import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='admin', db='python')
cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
sql = 'select * from userinfo'
cur.execute(sql)
print(cur.fetchone())
print(cur.fetchone())
cur.scroll(0,mode='absolute')#绝对定位，返回到0（就是第一行）
print(cur.fetchone())
cur.scroll(-1, mode='relative')#相对定位，返回到上一条
print(cur.fetchone())
print(cur.fetchall())


