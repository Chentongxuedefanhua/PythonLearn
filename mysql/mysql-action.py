#!/usr/bin/env python
# _*_coding:utf8_*_
# __auth:ChenFan

import MySQLdb

#创建连接
conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='admin', db='python')
#创建游标
cur = conn.cursor()
#操作数据库
#增
sql = 'insert into userinfo(id,name) value(%s,%s)'
params = ('4', 'jerry')
cur.execute(sql, params)#执行sql
conn.commit()#提交
#关闭数据库连接
cur.close()
conn.close()


