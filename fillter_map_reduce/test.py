#coding: utf-8

"""
@file: test.py
@time: 2017/8/30 
@author: chenfan
"""

####map,结果返回list
'''
map(function, sequence[, sequence, ...]) -> list
说明：
      对sequence中的item依次执行function(item)，执行结果输出为list。
'''
print map(str,range(5))

def add(n):
    return n+n
print map(add,range(5))

print map(lambda x:x+1, range(5))

def add2(x,y):
    return x+y
print map(add2, range(5), range(5,10))#长度一致


####reduce
'''
 reduce(function, sequence[, initial]) -> value
 说明：
      对sequence中的item顺序迭代调用function，函数必须要有2个参数。要是有第3个参数，则表示初始值，可以继续调用初始值，返回一个值。
'''
def add3(x, y):
    return x+y
print reduce(add3,range(10)) #0+1+2+...+9
print reduce(add3,range(10),20) #20为默认值，20+0+1+...+9=65

####filter
'''
filter(function or None, sequence) -> list, tuple, or string
说明：
      对sequence中的item依次执行function(item)，将执行结果为True（！=0）的item组成一个List/String/Tuple（取决于sequence的类型）返回，False则退出（0），进行过滤。
'''
def div(n):
    return n%2
print filter(div,range(5))
