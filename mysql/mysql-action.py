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
#删
sql2 = 'delete from userinfo where id=3'
cur.execute(sql2)
#改
sql3 = 'update userinfo SET name=%s where id=%s'
params2 = ('test', 4)
cur.execute(sql3, params2)
conn.commit()
#查
sql4 = 'select * from userinfo'
resec = cur.execute(sql4)#返回受影响的行数
data = cur.fetchall()#返回所有数据
print(resec)
print(data)
#关闭数据库连接
cur.close()
conn.close()


